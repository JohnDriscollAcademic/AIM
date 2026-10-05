#!/usr/bin/env python3
"""Catalogue integrity tests on disposable copies; standard library only."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from catalogue import next_problem_id, presentation_records, render_catalog, render_readme, render_resolved, subject_index
from markdown_math import expressions, validate_math

ROOT = Path(__file__).resolve().parents[1]
GENERATED = ('README.md', 'CATALOG.md', 'RESOLVED.md')
BADGES = {
    'Open': '🔵 OPEN',
    'Partially resolved': '🟡 PARTIAL',
    'Solution claimed': '🟠 SOLUTION CLAIMED',
    'Solved': '✅ SOLVED',
    'Lean verified': '🏆 LEAN VERIFIED',
    'Needs verification': '⚪ NEEDS VERIFICATION',
    'Withdrawn': '⚫ WITHDRAWN',
}
ARCHIVE_STATUSES = ('Lean verified', 'Solved', 'Solution claimed',
                    'Needs verification', 'Withdrawn')


class ResolutionPresentationTests(unittest.TestCase):
    def setUp(self):
        self.entries = [{'id': '001', 'title': 'Still open', 'area': 'Example',
                         'file': 'problems/001-open.md', 'status': 'Partially resolved',
                         'last_checked': '2026-01-01', 'group': 'first'}]
        self.solved = {'id': '002', 'title': 'A resolved target', 'group': 'first',
                       'status': 'Solved', 'last_checked': '2026-01-01',
                       'record': 'research/002.md', 'reason': 'Full review notes',
                       'outcome': 'Counterexample', 'proof': 'research/proof.md',
                       'review': 'research/review.md'}
        self.claim = {**self.solved, 'id': '003', 'title': 'An outstanding claim',
                      'status': 'Solution claimed', 'record': 'research/003.md'}
        self.lean = {**self.solved, 'id': '004', 'title': 'A formal proof',
                     'status': 'Lean verified', 'record': 'research/004.md',
                     'verification_record': 'research/lean-evidence.md'}
        self.manifest = {'groups': [{'key': 'first', 'title': 'First subject'},
                                    {'key': 'empty', 'title': 'Empty subject'}],
                         'batches': [{'title': 'Example', 'ids': ['001', '002', '003', '004']}],
                         'retired': [self.solved, self.claim, self.lean]}

    def test_counts_link_to_each_subject_list_and_exclude_claims(self):
        index = '\n'.join(subject_index(self.entries, self.manifest, 'CATALOG.md'))
        self.assertIn('| [First subject](CATALOG.md#first-subject) | '
                      '[1](CATALOG.md#first-open) | [2](CATALOG.md#first-solved) |', index)
        self.assertIn('[0](CATALOG.md#empty-open) | [0](CATALOG.md#empty-solved)', index)

    def test_catalogue_pairs_open_and_solved_and_separates_claims(self):
        text = render_catalog(self.entries, self.manifest)
        first = text.split('## First subject\n', 1)[1].split('\n## Empty subject', 1)[0]
        opened, solved = first.split('### Solved problems', 1)
        solved, claimed = solved.split('### Solution claimed', 1)
        self.assertIn('| 001 |', opened)
        self.assertNotIn('| 002 |', opened)
        self.assertIn('| 002 |', solved)
        self.assertIn('| 004 |', solved)
        self.assertNotIn('| 003 |', solved)
        self.assertIn('| 003 |', claimed)
        for group in self.manifest['groups']:
            for section in ('open', 'solved'):
                self.assertIn(f'<a name="{group["key"]}-{section}"></a>', text)
        self.assertIn('No solved problems are currently recorded in this subject.', text)

    def test_readme_shows_proofs_and_reviews_for_complete_resolutions(self):
        text = render_readme(self.entries, self.manifest)
        self.assertIn('| 002 |', text)
        self.assertIn('| 004 |', text)
        self.assertNotIn('| 001 |', text)
        self.assertNotIn('| 003 |', text)
        self.assertIn('| Counterexample | [Proof](research/proof.md) | [Review](research/review.md)', text)
        self.assertIn('[Lean evidence](research/lean-evidence.md)', text)

    def test_archive_starts_with_solved_and_omits_empty_statuses(self):
        text = render_resolved(self.manifest)
        self.assertLess(text.index('## Solved\n'), text.index('## Lean verified\n'))
        self.assertLess(text.index('## Lean verified\n'), text.index('## Solution claimed\n'))
        self.assertNotIn('## Needs verification\n', text)
        self.assertNotIn('## Withdrawn\n', text)
        self.assertIn('| Counterexample | 2026-01-01 | [Proof](research/proof.md) | [Review](research/review.md)', text)


class NumberAllocationTests(unittest.TestCase):
    def test_next_id_follows_current_collection(self):
        manifest = {'batches': [{'ids': ['001', '002']}], 'retired': []}
        self.assertEqual(next_problem_id(manifest), 3)

    def test_archive_ids_are_included(self):
        manifest = {'batches': [{'ids': ['001', '002', '003']}],
                    'retired': [{'id': '003'}]}
        self.assertEqual(next_problem_id(manifest), 4)

    def test_ids_above_three_digits_use_numeric_order(self):
        manifest = {'batches': [{'ids': ['998', '1000', '999']}],
                    'retired': []}
        self.assertEqual(next_problem_id(manifest), 1001)


class MathFormattingTests(unittest.TestCase):
    def test_protected_inline_and_display_preserve_tex(self):
        tex = r'\left\{x_1,x_2\right\}'
        content = '$`' + tex + '`$\n\n```math\n' + tex + '\n```\n'
        found, errors = expressions(content)
        self.assertEqual(errors, [])
        self.assertEqual([(e.tex, e.display) for e in found], [(tex, False), (tex, True)])
        self.assertEqual(validate_math(content), [])

    def test_unprotected_and_legacy_math_are_rejected(self):
        for content in ('$x$', '$$\nx\n$$', r'\(x\)', r'\[x\]'):
            with self.subTest(content=content):
                self.assertTrue(any('protect math' in error for error in validate_math(content)))

    def test_code_examples_and_escaped_dollars_are_not_math(self):
        content = '`$x$` and \\$5\n\n````markdown\n```math\nx\n```\n$x$\n````\n'
        self.assertEqual(expressions(content), ([], []))
        self.assertEqual(validate_math(content), [])

    def test_unclosed_math_and_fences_are_rejected(self):
        for content in ('$`x', '```math\nx\n', '$x'):
            with self.subTest(content=content):
                self.assertTrue(any('unclosed' in error for error in validate_math(content)))


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='aim-catalogue-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('data', 'problems', 'research', 'scripts', 'docs',
                     'lean-statements', 'tools', '.github'):
            shutil.copytree(ROOT / name, self.root / name,
                            ignore=shutil.ignore_patterns('.git', '.lake', '.venv',
                                                         '__pycache__'))
        for name in (*GENERATED, 'CONTRIBUTING.md', 'CITATION.cff', 'catalogue.json'):
            shutil.copy2(ROOT / name, self.root / name)

    def test_local_dependency_markdown_is_ignored(self):
        for directory in ('lean-statements/.lake/packages/example',
                          'research/lean/114/.lake/packages/example', '.venv'):
            path = self.root / directory / 'README.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('[missing](does-not-exist.md) and $unprotected$\n',
                            encoding='utf-8')
        self.run_catalogue()
        self.run_catalogue('--check')

    def test_source_markdown_remains_validated_with_caches_present(self):
        cached = self.root / '.lake' / 'README.md'
        cached.parent.mkdir()
        cached.write_text('[ignored](missing-cache-file.md)\n', encoding='utf-8')
        source = self.root / 'research' / 'cache-regression.md'
        source.write_text('[must fail](missing-source-file.md)\n', encoding='utf-8')
        self.run_catalogue(expected=1, message='missing-source-file.md')

    def test_uppercase_markdown_extension_preserves_platform_link_checks(self):
        source = self.root / 'research' / 'uppercase-regression.MD'
        source.write_text('[must fail](missing-uppercase-file.md)\n', encoding='utf-8')
        # Preserve pathlib's former default: Windows matches extensions without
        # regard to case; POSIX matches their case exactly.
        if os.name == 'nt':
            self.run_catalogue(expected=1, message='missing-uppercase-file.md')
        else:
            self.run_catalogue()

    def run_catalogue(self, mode='--write', expected=0, message=None):
        # Exercise default locale encodings even when the parent enables UTF-8 mode.
        result = subprocess.run([sys.executable, 'scripts/catalogue.py', mode],
                                cwd=self.root, capture_output=True, encoding="utf-8",
                                env={**os.environ, "PYTHONUTF8": "0",
                                     "PYTHONIOENCODING": "utf-8"})
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertNotIn('Traceback (most recent call last)', result.stderr)
        if message:
            self.assertIn(message, result.stdout)

    def read_json(self, name):
        return json.loads((self.root / name).read_text(encoding="utf-8"))

    def write_json(self, name, value):
        (self.root / name).write_text(json.dumps(value, indent=2) + '\n', encoding="utf-8")

    def problem_entries(self):
        manifest = self.read_json('catalogue.json')
        return [{**row, 'group': group['key']} for group in manifest['groups']
                for row in self.read_json(f"data/{group['key']}.json")]

    def active_entries(self):
        return [row for row in self.problem_entries()
                if row['status'] in ('Open', 'Partially resolved')]

    def section(self, text, heading):
        return text.split(f'## {heading}\n', 1)[1].split('\n## ', 1)[0]

    def change_row(self, edit):
        rows = self.read_json('data/spectral.json')
        edit(rows)
        self.write_json('data/spectral.json', rows)

    def change_page(self, edit):
        row = self.read_json('data/spectral.json')[0]
        path = self.root / row['file']
        path.write_text(edit(path.read_text(encoding="utf-8")), encoding="utf-8")

    def set_page_status(self, path, status):
        path.write_text(re.sub(r'^\*\*Status:\*\*.*$',
                               f'**Status:** {BADGES[status]}',
                               path.read_text(encoding="utf-8"), flags=re.MULTILINE), encoding="utf-8")

    def set_partial_page(self, path):
        self.set_page_status(path, 'Partially resolved')
        text = path.read_text(encoding="utf-8")
        notes = {
            'Known cases': 'The cited work establishes the target for balls.',
            'Remaining target': 'The target remains open for arbitrary admissible domains.',
        }
        for field, content in notes.items():
            if f'**{field}:**' not in self.section(text, 'Status review'):
                text = text.replace('## Status review\n',
                                    f'## Status review\n\n**{field}:** {content}\n', 1)
        path.write_text(text, encoding="utf-8")

    def set_application(self, body):
        self.change_page(lambda text: re.sub(
            r'(## Application\n).*?(?=\n## |\Z)',
            lambda match: match[1] + '\n' + body + '\n', text, flags=re.DOTALL))

    def add_retired_fixtures(self, statuses):
        manifest = self.read_json('catalogue.json')
        first_id = max(int(i) for batch in manifest['batches'] for i in batch['ids']) + 1
        original = self.read_json('data/spectral.json')[0]
        template = (self.root / original['file']).read_text(encoding="utf-8")
        fixtures = []
        for offset, status in enumerate(statuses):
            identifier = f'{first_id + offset:03d}'
            row = {'id': identifier, 'title': f'Temporary {status.lower()} target',
                   'group': 'spectral',
                   'status': status, 'last_checked': original['last_checked'],
                   'reason': f'Temporary review for {identifier}',
                   'record': f'research/test-{identifier}.md'}
            content = template.replace(f"# {original['id']}. {original['title']}",
                                       f"# {identifier}. {row['title']}", 1)
            path = self.root / row['record']
            path.write_text(content, encoding="utf-8")
            self.set_page_status(path, status)
            if status in ('Solved', 'Lean verified'):
                row['outcome'] = 'Affirmative proof'
                row['proof'] = f'research/test-{identifier}-proof.md'
                row['review'] = f'research/test-{identifier}-review.md'
                for field in ('proof', 'review'):
                    (self.root / row[field]).write_text(f'# Synthetic {field} fixture\n', encoding='utf-8')
            if status == 'Lean verified':
                row['verification_record'] = f'research/test-{identifier}-lean.md'
                (self.root / row['verification_record']).write_text(
                    '# Lean verification evidence\n\n'
                    'Synthetic fixture: theorem name, proof commit, Lean version, '
                    'build command and successful output are documented here.\n', encoding="utf-8")
            manifest['retired'].append(row)
            fixtures.append(row)
        manifest['batches'].append({'key': 'retained-test', 'title': 'Retained test',
                                   'ids': [row['id'] for row in fixtures]})
        self.write_json('catalogue.json', manifest)
        return fixtures

    def test_baseline_and_preservation(self):
        originals = {p.relative_to(self.root): p.read_bytes()
                     for p in (self.root / 'problems').glob('*.md')}
        self.run_catalogue()
        self.run_catalogue('--check')
        self.assertTrue(all((self.root / p).read_bytes() == text
                            for p, text in originals.items()))

    def test_open_and_solved_browsing(self):
        self.run_catalogue()
        readme = (self.root / 'README.md').read_text(encoding="utf-8")
        catalogue = (self.root / 'CATALOG.md').read_text(encoding="utf-8")
        resolved = (self.root / 'RESOLVED.md').read_text(encoding="utf-8")
        entries, manifest = presentation_records(self.problem_entries(), self.read_json('catalogue.json'))
        self.assertTrue(readme.startswith('# AIM — Open Applied Problems\n'))
        self.assertIn(f'**{len(entries)} open targets**', readme)
        self.assertIn('](CATALOG.md)', readme)
        self.assertIn('](RESOLVED.md)', readme)
        self.assertIn('](CITATION.cff)', readme)
        solved_ids = {row['id'] for row in manifest['retired']
                      if row['status'] in ('Solved', 'Lean verified')}
        self.assertEqual(set(re.findall(r'(?m)^\| (\d{3,}) \|', readme)), solved_ids)
        self.assertNotIn('| Publication batch |', readme)
        self.assertIn('| Publication batch |', catalogue)
        self.assertEqual(manifest['schema_version'], 2)
        self.assertIn('| Status |', catalogue)
        for group in manifest['groups']:
            self.assertNotIn(f"## {group['title']}\n", readme)
            section = self.section(catalogue, group['title'])
            open_rows = [row for row in entries if row['group'] == group['key']]
            solved_count = sum(row['group'] == group['key'] and row['id'] in solved_ids
                               for row in manifest['retired'])
            self.assertIn(f"[{len(open_rows)}](CATALOG.md#{group['key']}-open) | "
                          f"[{solved_count}](CATALOG.md#{group['key']}-solved)", readme)
            self.assertIn(f'<a name="{group["key"]}-open"></a>', section)
            self.assertIn(f'<a name="{group["key"]}-solved"></a>', section)
            self.assertLess(section.index('### Open problems'), section.index('### Solved problems'))
            for row in open_rows:
                self.assertIn(f"| {row['id']} |", section)
                self.assertIn(f"]({row['file']})", section)
                line = next(line for line in section.splitlines()
                            if line.startswith(f"| {row['id']} |"))
                self.assertIn(BADGES[row['status']], line)
        for row in manifest['retired']:
            group = next(group for group in manifest['groups'] if group['key'] == row['group'])
            self.assertIn(f"| {row['id']} |", self.section(catalogue, group['title']))
            self.assertIn(f"| {row['id']} |", resolved)
            self.assertIn(f"]({row['record']})", resolved)
            line = next(line for line in resolved.splitlines()
                        if line.startswith(f"| {row['id']} |"))
            self.assertIn(BADGES[row['status']], line)
            if row['id'] in solved_ids:
                for text in (readme, catalogue, resolved):
                    line = next(line for line in text.splitlines() if line.startswith(f"| {row['id']} |"))
                    self.assertIn(row['outcome'], line)
                    self.assertIn(f"[Proof]({row['proof']})", line)
                    self.assertIn(f"[Review]({row['review']})", line)
            if row['status'] == 'Solution claimed':
                self.assertIn(f"| {row['id']} |", self.section(resolved, 'Solution claimed'))
                self.assertNotIn(f"| {row['id']} |", self.section(resolved, 'Solved'))
        for status in ARCHIVE_STATUSES:
            if not any(row['status'] == status for row in manifest['retired']):
                self.assertNotIn(f'## {status}\n', resolved)

    def test_duplicate_id(self):
        self.change_row(lambda rows: rows.append(dict(rows[0])))
        self.run_catalogue(expected=1, message='Duplicate ID')

    def test_duplicate_file(self):
        self.change_row(lambda rows: rows[1].update(file=rows[0]['file']))
        self.run_catalogue(expected=1, message='Duplicate file')

    def test_missing_metadata(self):
        self.change_row(lambda rows: rows[0].pop('status'))
        self.run_catalogue(expected=1, message='incomplete metadata')

    def test_invalid_active_status(self):
        original = self.read_json('data/spectral.json')
        path = self.root / original[0]['file']
        original_page = path.read_text(encoding="utf-8")
        for status in (*ARCHIVE_STATUSES, 'open', 'Retired', '', '   ', None, 123, [], {}):
            with self.subTest(status=status):
                self.write_json('data/spectral.json', original)
                path.write_text(original_page, encoding="utf-8")
                self.change_row(lambda rows: rows[0].update(status=status))
                if isinstance(status, str) and status in BADGES:
                    self.set_page_status(path, status)
                self.run_catalogue(expected=1)

    def test_partial_status_remains_in_open_catalogue_and_count(self):
        row = self.read_json('data/spectral.json')[0]
        self.change_row(lambda rows: rows[0].update(status='Partially resolved'))
        self.set_partial_page(self.root / row['file'])
        self.run_catalogue()
        self.run_catalogue('--check')
        catalogue = (self.root / 'CATALOG.md').read_text(encoding="utf-8")
        line = next(line for line in catalogue.splitlines()
                    if line.startswith(f"| {row['id']} |"))
        self.assertIn('🟡 PARTIAL', line)
        self.assertNotIn(f"| {row['id']} |", (self.root / 'RESOLVED.md').read_text(encoding="utf-8"))
        self.assertIn(f'**{len(self.active_entries())} open targets**',
                      (self.root / 'README.md').read_text(encoding="utf-8"))

    def test_partial_status_requires_known_cases_and_remaining_target(self):
        row = self.read_json('data/spectral.json')[0]
        self.change_row(lambda rows: rows[0].update(status='Partially resolved'))
        path = self.root / row['file']
        self.set_partial_page(path)
        original = path.read_text(encoding="utf-8")
        for field in ('Known cases', 'Remaining target'):
            for change in ('missing', 'empty', 'outside review'):
                with self.subTest(field=field, change=change):
                    pattern = rf'^\*\*{field}:\*\*.*\n'
                    content = re.search(pattern, original, re.MULTILINE)[0]
                    replacement = f'**{field}:** \n' if change == 'empty' else ''
                    text = re.sub(pattern, replacement, original, flags=re.MULTILINE)
                    if change == 'outside review':
                        text = text.replace('## Problem statement\n',
                                            f'## Problem statement\n\n{content}', 1)
                    path.write_text(text, encoding="utf-8")
                    self.run_catalogue(expected=1,
                                       message=f'Partial requires {field} in Status review')

    def test_status_badge_must_match_metadata(self):
        row = self.read_json('data/spectral.json')[0]
        path = self.root / row['file']
        original = path.read_text(encoding="utf-8")
        for badge in ('Open', BADGES['Solved'], '', '🔵 OPEN in cited literature',
                      BADGES[row['status']] + '.'):
            with self.subTest(badge=badge):
                path.write_text(re.sub(r'^\*\*Status:\*\*.*$',
                                       '**Status:** ' + badge,
                                       original, flags=re.MULTILINE), encoding="utf-8")
                self.run_catalogue(expected=1)

    def test_status_badge_must_precede_first_section(self):
        def move_status(text):
            line = re.search(r'^\*\*Status:\*\*.*$', text, re.MULTILINE)[0]
            text = text.replace(line + '\n', '', 1)
            return text.replace('## Status review\n', '## Status review\n\n' + line, 1)
        self.change_page(move_status)
        self.run_catalogue(expected=1)

    def test_missing_status_badge(self):
        self.change_page(lambda text: re.sub(r'^\*\*Status:\*\*.*\n', '',
                                            text, flags=re.MULTILINE))
        self.run_catalogue(expected=1)

    def test_missing_application(self):
        self.change_page(lambda text: text.replace('## Application\n', '## Motivation\n'))
        self.run_catalogue(expected=1, message='missing Application')

    def test_empty_or_placeholder_application(self):
        for body in ('', '   \n\t', 'TODO', 'TBD', 'N/A'):
            with self.subTest(body=body):
                self.set_application(body)
                self.run_catalogue(expected=1)

    def test_application_prose_is_preserved(self):
        body = ('A positive result would give rigorous frequency bounds for vibrating '
                'structures from geometric information, supporting resonance avoidance.')
        self.set_application(body)
        self.run_catalogue()
        row = self.read_json('data/spectral.json')[0]
        self.assertIn(body, (self.root / row['file']).read_text(encoding="utf-8"))

    def test_missing_heading(self):
        self.change_page(lambda text: text.replace('## References', '## Reading'))
        self.run_catalogue(expected=1, message='missing References')

    def test_math_requires_markdown_protection(self):
        row = self.read_json('data/spectral.json')[0]
        path = self.root / row['file']
        original = path.read_text(encoding="utf-8")
        for block in ('Before\n$$\nx^2\n$$\n\nAfter',
                      'Before\n\n$$\nx^2\n$$\nAfter',
                      'Before\n\n$$x^2$$\n\nAfter',
                      'Before\n\n$$\nx^2\n$$\n$$\ny^2\n$$\n\nAfter'):
            with self.subTest(block=block):
                path.write_text(original + '\n' + block + '\n', encoding="utf-8")
                self.run_catalogue(expected=1, message='protect math')

    def test_protected_display_and_inline_math(self):
        self.change_page(lambda text: text + '\nBefore $`x^2`$.\n\n```math\ny^2\n```\n\nAfter\n')
        self.run_catalogue('--check')

    def test_math_protection_applies_to_research_files(self):
        (self.root / 'research/math-regression.md').write_text(
            r'An unsafe expression: $\left\{x\right\}$.', encoding='utf-8')
        self.run_catalogue(expected=1, message='research/math-regression.md: line 1: protect math')

    def test_unsupported_math_operator_names(self):
        row = self.read_json('data/spectral.json')[0]
        path = self.root / row['file']
        original = path.read_text(encoding="utf-8")
        for expression in (r'$`\operatorname{Per}(E)`$',
                           '\n```math\n' + r'\operatorname*{ess\,sup}_t f(t)' + '\n```\n'):
            with self.subTest(expression=expression):
                path.write_text(original + '\n' + expression + '\n', encoding="utf-8")
                self.run_catalogue(expected=1, message='unsupported operator-name macro')

    def test_metadata_mismatch(self):
        self.change_row(lambda rows: rows[0].update(area='Incorrect area'))
        self.run_catalogue(expected=1, message='inconsistent Area')

    def test_unindexed_page(self):
        (self.root / 'problems/unindexed.md').write_text('# Unindexed\n', encoding="utf-8")
        self.run_catalogue(expected=1, message='Unindexed problem file')

    def test_missing_page(self):
        row = self.read_json('data/spectral.json')[0]
        (self.root / row['file']).unlink()
        self.run_catalogue(expected=1, message='Missing problems/')

    def test_invalid_date(self):
        self.change_row(lambda rows: rows[0].update(last_checked='2026-02-30'))
        self.run_catalogue(expected=1, message='invalid ISO date')

    def test_future_date(self):
        self.change_row(lambda rows: rows[0].update(last_checked='9999-01-01'))
        self.run_catalogue(expected=1, message='status check is in the future')

    def test_broken_local_link(self):
        self.change_page(lambda text: text + '\n[Missing](../missing.md)\n')
        self.run_catalogue(expected=1, message='broken local link')

    def test_stale_outputs_are_detected_and_regenerated(self):
        self.run_catalogue()
        for name in GENERATED:
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_text(encoding="utf-8")
                path.write_text(original + 'Stale output\n', encoding="utf-8")
                self.run_catalogue('--check', expected=1, message=f'{name} is stale')
                self.run_catalogue()
                self.assertEqual(path.read_text(encoding="utf-8"), original)
                self.run_catalogue('--check')

    def test_missing_outputs_are_detected_and_regenerated(self):
        self.run_catalogue()
        originals = {name: (self.root / name).read_text(encoding="utf-8") for name in GENERATED}
        for name in GENERATED:
            with self.subTest(name=name):
                (self.root / name).unlink()
                self.run_catalogue('--check', expected=1, message=f'{name} is missing')
                self.run_catalogue()
                self.assertEqual((self.root / name).read_text(encoding="utf-8"), originals[name])
                self.run_catalogue('--check')
        for name in GENERATED:
            (self.root / name).unlink()
        self.run_catalogue('--check', expected=1, message='README.md is missing')
        self.run_catalogue()
        for name in GENERATED:
            self.assertEqual((self.root / name).read_text(encoding="utf-8"), originals[name])
        self.run_catalogue('--check')

    def test_noncontiguous_grouping_and_counts(self):
        manifest = self.read_json('catalogue.json')
        grouped = {group['key']: self.read_json(f"data/{group['key']}.json")
                   for group in manifest['groups']}
        moved = sorted(self.active_entries(), key=lambda row: int(row['id']))[-3:]
        ids = [row['id'] for row in moved]
        for rows in grouped.values():
            rows[:] = [row for row in rows if row['id'] not in ids]
        for row, stem in zip(moved, ('spectral', 'operators', 'spectral')):
            grouped[stem].append(row)
        for stem, rows in grouped.items():
            self.write_json(f'data/{stem}.json', rows)
        self.run_catalogue()
        self.run_catalogue('--check')
        readme = (self.root / 'README.md').read_text(encoding="utf-8")
        catalogue = (self.root / 'CATALOG.md').read_text(encoding="utf-8")
        spectral = self.section(catalogue, 'Spectral theory and spectral geometry')
        operators = self.section(catalogue, 'Operators, matrices and computation')
        self.assertIn(f'| {ids[0]} |', spectral)
        self.assertIn(f'| {ids[2]} |', spectral)
        self.assertNotIn(f'| {ids[1]} |', spectral)
        self.assertIn(f'| {ids[1]} |', operators)
        self.assertIn(f'**{len(self.active_entries())} open targets**', readme)
        for identifier in ids:
            self.assertNotIn(f'| {identifier} |', readme)
        spectral_count = sum(row['status'] in ('Open', 'Partially resolved') for row in grouped['spectral'])
        self.assertIn(f'[{spectral_count}](CATALOG.md#spectral-open)', readme)

    def test_missing_batch_membership(self):
        manifest = self.read_json('catalogue.json')
        manifest['batches'][0]['ids'].pop()
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1, message='batches must partition')

    def test_unregistered_metadata(self):
        self.write_json('data/unregistered.json', [])
        self.run_catalogue(expected=1, message='Unregistered metadata')

    def test_retired_id_cannot_be_reused(self):
        self.add_retired_fixtures(('Solution claimed',))
        manifest = self.read_json('catalogue.json')
        row = dict(manifest['retired'][0])
        row['id'] = '001'
        manifest['retired'].append(row)
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1, message='Duplicate ID')

    def test_deleted_ids_cannot_be_reserved(self):
        manifest = self.read_json('catalogue.json')
        manifest['removed_ids'] = ['002']
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1, message='deleted IDs cannot be reserved')

    def test_removed_ids_require_valid_identifiers(self):
        original = self.read_json('catalogue.json')
        for value in (None, '031', ['000'], ['31'], [31], [{}]):
            with self.subTest(value=value):
                manifest = dict(original, removed_ids=value)
                self.write_json('catalogue.json', manifest)
                self.run_catalogue(expected=1, message='removed_ids must be an array of valid IDs')

    def test_gap_in_active_numbering_is_rejected(self):
        self.change_row(lambda rows: rows.pop(1))
        self.run_catalogue(expected=1, message='Active problem IDs must be consecutive')

    def test_solved_page_keeps_its_id_and_path(self):
        rows = self.read_json('data/spectral.json')
        row = rows[0]
        row.update(status='Solved', outcome='Affirmative proof',
                   proof='https://example.com/proof', review='https://example.com/review')
        self.write_json('data/spectral.json', rows)
        self.set_page_status(self.root / row['file'], 'Solved')
        self.run_catalogue()
        self.run_catalogue('--check')
        self.assertTrue((self.root / row['file']).is_file())
        self.assertEqual(self.read_json('data/spectral.json')[0]['id'], row['id'])
        self.assertNotIn(row['id'], [r['id'] for r in self.read_json('catalogue.json')['retired']])
        readme = (self.root / 'README.md').read_text(encoding='utf-8')
        catalogue = (self.root / 'CATALOG.md').read_text(encoding='utf-8')
        resolved = (self.root / 'RESOLVED.md').read_text(encoding='utf-8')
        self.assertIn(f'**{len(self.active_entries())} open targets**', readme)
        for text in (readme, catalogue, resolved):
            self.assertIn(f"[{row['title']}]({row['file']}) | ✅ SOLVED", text)
        self.assertNotIn(f"| {row['id']} |", catalogue.split('### Solved problems', 1)[0])
        original = dict(row)
        for field in ('outcome', 'proof', 'review'):
            rows[0] = {k: v for k, v in original.items() if k != field}
            self.write_json('data/spectral.json', rows)
            self.run_catalogue(expected=1, message=f'Solved requires a {field} link' if field != 'outcome' else 'Solved requires an outcome')

    def test_documented_retirement_preserves_id(self):
        manifest = self.read_json('catalogue.json')
        all_rows = [(group['key'], row) for group in manifest['groups']
                    for row in self.read_json(f"data/{group['key']}.json")]
        stem, row = max(all_rows, key=lambda pair: int(pair[1]['id']))
        rows = self.read_json(f'data/{stem}.json')
        self.write_json(f'data/{stem}.json', [r for r in rows if r['id'] != row['id']])
        old_path = self.root / row['file']
        record = f"research/retired-{row['id']}.md"
        old_path.rename(self.root / record)
        self.set_page_status(self.root / record, 'Withdrawn')
        for path in self.root.rglob('*.md'):
            content = path.read_text(encoding="utf-8").replace(row['file'], record)
            if path == self.root / record:
                # Moving the fixture changes the base of sibling problem links.
                content = re.sub(r'\]\((\d{3,}-[^/)]+\.md)(#[^)]*)?\)',
                                 r'](../problems/\1\2)', content)
            if path.parent == self.root / 'problems':
                content = content.replace(f']({old_path.name})', f'](../{record})')
            path.write_text(content, encoding="utf-8")
        manifest['retired'].append({'id': row['id'], 'title': row['title'],
                                    'group': stem,
                                    'status': 'Withdrawn', 'last_checked': row['last_checked'],
                                    'reason': 'Test only', 'record': record})
        self.write_json('catalogue.json', manifest)
        self.run_catalogue()
        self.run_catalogue('--check')
        resolved = (self.root / 'RESOLVED.md').read_text(encoding="utf-8")
        self.assertIn(f"[{row['title']}]({record})",
                      self.section(resolved, 'Withdrawn'))
        self.assertIn('⚫ WITHDRAWN', self.section(resolved, 'Withdrawn'))
        for retired in manifest['retired']:
            if retired['status'] == 'Solution claimed':
                self.assertIn(f"| {retired['id']} |", self.section(resolved, 'Solution claimed'))
        self.assertIn(f'**{len(self.active_entries())} open targets**',
                      (self.root / 'README.md').read_text(encoding="utf-8"))

    def test_retained_status_sections(self):
        fixtures = self.add_retired_fixtures(ARCHIVE_STATUSES)
        self.run_catalogue()
        self.run_catalogue('--check')
        resolved = (self.root / 'RESOLVED.md').read_text(encoding="utf-8")
        catalogue = (self.root / 'CATALOG.md').read_text(encoding="utf-8")
        for row in fixtures:
            with self.subTest(status=row['status']):
                section = self.section(resolved, row['status'])
                self.assertIn(f"| {row['id']} |", section)
                self.assertIn(f"[{row['title']}]({row['record']})", section)
                self.assertIn(row.get('outcome', row['reason']), section)
                self.assertIn('| Status |', section)
                self.assertIn(BADGES[row['status']], section)
                self.assertIn(f"| {row['id']} |", catalogue)
                if row['status'] == 'Lean verified':
                    self.assertIn(f"]({row['verification_record']})", section)
                for other_heading in ARCHIVE_STATUSES:
                    if other_heading != row['status']:
                        self.assertNotIn(f"| {row['id']} |",
                                         self.section(resolved, other_heading))
        readme = (self.root / 'README.md').read_text(encoding="utf-8")
        self.assertIn(f'**{len(self.active_entries())} open targets**', readme)
        _, display_manifest = presentation_records(self.problem_entries(), self.read_json('catalogue.json'))
        retired = display_manifest['retired']
        solved = sum(row['status'] == 'Solved' for row in retired)
        lean = sum(row['status'] == 'Lean verified' for row in retired)
        claimed = sum(row['status'] == 'Solution claimed' for row in retired)
        self.assertIn(f'**{solved} solved entr', readme)
        self.assertIn(f'**{lean} Lean verified', readme)
        self.assertIn(f"**{claimed} solution claim{'s' if claimed != 1 else ''}**", readme)
        self.assertNotIn('## Other retained entries', resolved)

    def test_invalid_retirement_metadata(self):
        self.add_retired_fixtures(('Solution claimed',))
        for field, values in (('title', ('', '   ', None, 123)),
                              ('group', ('unregistered-subject', None, [])),
                              ('outcome', ('', None)),
                              ('proof', ('research/missing-proof.md', 'research/', None)),
                              ('review', ('research/missing-review.md', None)),
                              ('status', ('', 'solved', 'Open', 'Partially resolved',
                                          'Retired', None, 123, [], {}))):
            for value in values:
                with self.subTest(field=field, value=value):
                    manifest = self.read_json('catalogue.json')
                    original = dict(manifest['retired'][0])
                    manifest['retired'][0][field] = value
                    self.write_json('catalogue.json', manifest)
                    self.run_catalogue(expected=1, message=f'invalid retired {field}')
                    manifest['retired'][0] = original
                    self.write_json('catalogue.json', manifest)

    def test_missing_retirement_metadata(self):
        self.add_retired_fixtures(('Solution claimed',))
        original = self.read_json('catalogue.json')
        for field in ('id', 'title', 'group', 'status', 'last_checked', 'reason', 'record',
                      'outcome', 'proof', 'review'):
            with self.subTest(field=field):
                manifest = json.loads(json.dumps(original))
                manifest['retired'][0].pop(field)
                self.write_json('catalogue.json', manifest)
                self.run_catalogue(expected=1)

    def test_retired_page_metadata_must_match(self):
        self.add_retired_fixtures(('Solution claimed',))
        manifest = self.read_json('catalogue.json')
        row = manifest['retired'][0]
        path = self.root / row['record']
        original = path.read_text(encoding="utf-8")
        edits = {
            'title': lambda text: text.replace(row['title'], 'Wrong title', 1),
            'id': lambda text: text.replace(f"# {row['id']}.", '# 999.', 1),
            'status': lambda text: text.replace(BADGES[row['status']], BADGES['Open'], 1),
            'date': lambda text: text.replace(row['last_checked'], '2000-01-01'),
            'area': lambda text: re.sub(r'^\*\*Area:\*\*.*$', '**Area:** ',
                                        text, flags=re.MULTILINE),
        }
        for field, edit in edits.items():
            with self.subTest(field=field):
                path.write_text(edit(original), encoding="utf-8")
                self.run_catalogue(expected=1)

    def test_retired_page_requires_complete_sections(self):
        self.add_retired_fixtures(('Solution claimed',))
        row = self.read_json('catalogue.json')['retired'][0]
        path = self.root / row['record']
        original = path.read_text(encoding="utf-8")
        for heading in ('Problem statement', 'Application', 'References', 'Status review'):
            with self.subTest(heading=heading):
                path.write_text(original.replace(f'## {heading}\n', '## Removed\n'), encoding="utf-8")
                self.run_catalogue(expected=1, message=f'missing {heading}')

    def test_retired_application_cannot_be_empty(self):
        self.add_retired_fixtures(('Solution claimed',))
        row = self.read_json('catalogue.json')['retired'][0]
        path = self.root / row['record']
        path.write_text(re.sub(r'(## Application\n).*?(?=\n## |\Z)',
                               r'\1\n   \n', path.read_text(encoding="utf-8"), flags=re.DOTALL), encoding="utf-8")
        self.run_catalogue(expected=1)

    def test_lean_verification_record_is_required(self):
        self.add_retired_fixtures(('Lean verified',))
        manifest = self.read_json('catalogue.json')
        manifest['retired'][-1].pop('verification_record')
        self.write_json('catalogue.json', manifest)
        self.run_catalogue(expected=1)

    def test_lean_verification_record_must_be_nonempty_local_markdown(self):
        row = self.add_retired_fixtures(('Lean verified',))[0]
        manifest = self.read_json('catalogue.json')
        path = self.root / row['verification_record']
        for value in ('', '   \n'):
            with self.subTest(contents=value):
                path.write_text(value, encoding="utf-8")
                self.run_catalogue(expected=1)
        path.unlink()
        self.run_catalogue(expected=1)
        for value in ('https://example.com/proof.md', 'research/proof.txt', None, [], {}):
            with self.subTest(record=value):
                manifest['retired'][-1]['verification_record'] = value
                self.write_json('catalogue.json', manifest)
                if value == 'research/proof.txt':
                    (self.root / value).write_text('This is not a Markdown evidence record.\n', encoding="utf-8")
                self.run_catalogue(expected=1)


if __name__ == '__main__':
    unittest.main()
