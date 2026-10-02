"""Exact arithmetic verifier for a positive periodic Lotka--Volterra solution.

Finite products use signed 26-bit digits and int64 matrix products, with every
partial sum proved smaller than 2**63 in magnitude. A direct Python-integer
implementation is available for independent checking. Verification uses no
floating-point arithmetic; floating-point conversions only print diagnostics.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys
import numpy as np

AINT=np.array([[-224,-2551,-1969,454],[6814,-682,-1358,-11601],[7845,-808,-1695,-16707],[328,3248,5200,-685]],dtype=np.int64)


def complex_parts(ints,M):
    cr=np.zeros((4,M+1),dtype=np.int64);ci=cr.copy()
    for i in range(4):
        b=1+i*(2*M+1);cr[i,0]=ints[b]
        cr[i,1:]=ints[b+1:b+2*M+1:2];ci[i,1:]=ints[b+2:b+2*M+1:2]
    return cr,ci


def exact_jacobian(A,ints,Q,M,N,tail):
    """All entries of J are integers divided by 1000*Q."""
    n=1+4*(2*N+1);bs=2*N+1;D=1000*Q
    cr,ci=complex_parts(ints,M);omega=int(ints[0])
    # Object arrays prevent unnoticed integer overflow during construction.
    cr=cr.astype(object);ci=ci.astype(object);A=A.astype(object)
    Kr=np.zeros((4,4,M+1),dtype=object);Ki=Kr.copy()
    ar=A@cr;ai=A@ci
    for i in range(4):
      for j in range(4):
        Kr[i,j]=A[i,j]*cr[i];Ki[i,j]=A[i,j]*ci[i]
        if i==j:Kr[i,j]+=ar[i];Ki[i,j]+=ai[i]
        Kr[i,j,0]+=int(A[i,j])*Q
    def K(i,j,k):
        if abs(k)>M:return 0,0
        return int(Kr[i,j,abs(k)]),int(Ki[i,j,abs(k)])*(1 if k>=0 else -1)
    J=np.zeros((n,n+8*tail),dtype=np.int64);J[0,3]=D
    for i in range(4):
      bi=1+i*bs
      for k in range(1,min(N,M)+1):
        J[bi+2*k-1,0]=-k*int(ci[i,k])*1000
        J[bi+2*k,0]=k*int(cr[i,k])*1000
      for j in range(4):
        bj=1+j*bs
        for k in range(N+1):
          rr=bi if k==0 else bi+2*k-1;ri=bi+2*k
          pr,pi=K(i,j,k);J[rr,bj]=-pr
          if k:J[ri,bj]=-pi
          for l in range(1,N+tail+1):
            ca=bj+2*l-1 if l<=N else n+j*2*tail+2*(l-N)-2
            cb=ca+1
            pr,pi=K(i,j,k-l);qr,qi=K(i,j,k+l)
            zar=-(pr+qr);zai=-(pi+qi)
            zbr=pi-qi;zbi=-(pr-qr)
            if i==j and l==k:
                zai+=k*omega*1000;zbr-=k*omega*1000
            J[rr,ca]=zar;J[rr,cb]=zbr
            if k:J[ri,ca]=zai;J[ri,cb]=zbi
    return J,Kr,Ki


def exact_residual(A,ints,Q,M,N):
    """F(anchor) as integers with denominator 1000*Q**2."""
    n=1+4*(2*N+1);bs=2*N+1;fr=np.zeros((4,N+1),dtype=object);fi=fr.copy()
    cr,ci=complex_parts(ints,M);cr=cr.astype(object);ci=ci.astype(object);A=A.astype(object)
    er=np.concatenate([cr[:,1:][:,::-1],cr],axis=1)
    ei=np.concatenate([-ci[:,1:][:,::-1],ci],axis=1)
    ar=A@er;ai=A@ei;omega=int(ints[0])
    for i in range(4):
        # np.convolve with object arrays performs Python integer arithmetic.
        qr=np.convolve(er[i],ar[i])-np.convolve(ei[i],ai[i])
        qi=np.convolve(er[i],ai[i])+np.convolve(ei[i],ar[i])
        for k in range(min(N,2*M)+1):
            fr[i,k]=-qr[2*M+k];fi[i,k]=-qi[2*M+k]
            if k<=M:
                fr[i,k]+=-k*omega*int(ci[i,k])*1000-int(ar[i,M+k])*Q
                fi[i,k]+= k*omega*int(cr[i,k])*1000-int(ai[i,M+k])*Q
    out=np.zeros(n,dtype=object);out[0]=int(ci[0,1])*1000*Q
    for i in range(4):
        b=1+i*bs;out[b]=fr[i,0]
        out[b+1:b+2*N+1:2]=fr[i,1:];out[b+2:b+2*N+1:2]=fi[i,1:]
        assert fi[i,0]==0
    return out


def exact_matmul(a,b,method='int64',progress=True):
    """EXACT integer matrix product.

    Signed base-2**26 digits have absolute value at most 2**26-1.
    The asserted bound makes every product and every partial sum fit
    in int64. The resulting digit products are combined as arbitrary-
    precision Python integers. No floating-point arithmetic is used.
    method='python' provides a slower independent implementation.
    """
    assert a.ndim==2 and b.ndim==2 and a.shape[1]==b.shape[0]
    if method=='python': return a.astype(object)@b.astype(object)
    assert method=='int64'
    assert a.dtype==np.int64 and b.dtype==np.int64
    assert np.min(a)>np.iinfo(np.int64).min and np.min(b)>np.iinfo(np.int64).min
    bits=26;mask=(1<<bits)-1
    assert a.shape[1]*mask**2<2**63
    def digits(x):
        sign=np.sign(x);u=np.abs(x);z=[]
        while np.any(u):
            z.append((u & mask)*sign);u=u>>bits
        return z
    aa=digits(a);bb=digits(b)
    out=np.zeros((a.shape[0],b.shape[1]),dtype=object)
    for i,x in enumerate(aa):
      for j,y in enumerate(bb):
        product=x@y
        out+=product.astype(object)*(1<<bits*(i+j))
        if progress: print('exact integer digit product',i,j,flush=True)
    return out


def weighted_groups(N,tail=0):
    n=1+4*(2*N+1);bs=2*N+1
    outgroups=[np.array([0])]+[np.arange(1+i*bs,1+(i+1)*bs) for i in range(4)]
    ingroups=[np.array([0])]+[np.r_[np.arange(1+i*bs,1+(i+1)*bs),np.arange(n+2*i*tail,n+2*(i+1)*tail)] for i in range(4)]
    w=np.ones(n+8*tail,dtype=np.int64)*2;w[0]=1
    for i in range(4):w[1+i*bs]=1
    return outgroups,ingroups,w


def exact_block_norms(Mat,N,tail=0):
    """Integer numerators for weighted block norm, denominator TWO.
    Mat contains exact integers; if it represents a matrix /D,
    the returned array represents block norms /(2*D).
    """
    outg,ing,w=weighted_groups(N,tail);B=np.zeros((5,5),dtype=object)
    for a,I in enumerate(outg):
        sums=np.sum(np.abs(Mat[I,:].astype(object))*w[I,None],axis=0)
        for b,J in enumerate(ing):B[a,b]=int(np.max(sums[J]*(2//w[J])))
    return B


def vector_norm(v,N):
    """Weighted max-block l1 norm, integer numerator only."""
    bs=2*N+1
    return max(abs(int(v[0])),*[abs(int(v[1+i*bs]))+2*sum(abs(int(z)) for z in v[2+i*bs:1+(i+1)*bs]) for i in range(4)])


def certify(path=Path(__file__).with_name('fourier_certificate.npz'),method='int64'):
    z=np.load(path,allow_pickle=False);M=int(z['M']);N=int(z['N'])
    assert M==48 and N==128
    Q=2**int(z['den_exp']);RQ=2**int(z['R_den_exp'])
    assert Q==2**46 and RQ==2**40
    ints=z['coeffints'];R=z['Rints'];n=1+4*(2*N+1)
    assert ints.dtype==np.int64 and R.dtype==np.int64
    assert ints.shape==(1+4*(2*M+1),) and R.shape==(n,n)
    assert np.array_equal(z['Aint'],AINT)
    assert int(ints[0])==56183263666306
    omega=F(int(ints[0]),Q)
    J,Kr,Ki=exact_jacobian(AINT,ints,Q,M,N,M)
    print('exact J built','max',np.max(np.abs(J)),flush=True)
    E=-exact_matmul(R,J,method=method)
    JD=1000*Q;ED=RQ*JD
    for i in range(n):E[i,i]+=ED
    Bint=exact_block_norms(E,N,tail=M)
    B=[[F(int(v),2*ED) for v in row] for row in Bint]
    # Core-only Neumann bound certifies invertibility of R and of core J.
    Bcore=exact_block_norms(E[:,:n],N)
    neumann=max(F(sum(int(x) for x in row),2*ED) for row in Bcore)
    assert neumann<F(1,10**7)
    del E,J
    # Tail K norms and tail/core derivative bound.
    L=np.abs(Kr[:,:,0])+2*np.sum(np.abs(Kr[:,:,1:])+np.abs(Ki[:,:,1:]),axis=2)
    tau=[F(sum(int(v) for v in row),JD)/((N+1)*omega) for row in L]
    Z1=max(sum(row)+(F(0) if i==0 else tau[i-1]) for i,row in enumerate(B))
    # Newton residual, exactly.
    f=exact_residual(AINT,ints,Q,M,N)
    rf=R.astype(object)@f
    Y=F(vector_norm(rf,N),RQ*1000*Q**2)
    # Norm of R and R times Fourier differentiation, exactly.
    RB=exact_block_norms(R,N)
    RK=np.zeros(R.shape,dtype=object)
    for i in range(4):
      b=1+i*(2*N+1)
      for k in range(1,N+1):
        RK[:,b+2*k-1]=k*R[:,b+2*k].astype(object)
        RK[:,b+2*k]=-k*R[:,b+2*k-1].astype(object)
    RKB=exact_block_norms(RK,N);rows=[F(int(sum(abs(v) for v in row)),1000) for row in AINT]
    Z2=2*max(sum(F(int(v),2*RQ) for v in RKB[i,1:])+sum(F(int(RB[i,j+1]),2*RQ)*rows[j] for j in range(4))+(F(0) if i==0 else (1+rows[i-1]/(N+1))/omega) for i in range(5))
    # Clean rational inequalities stated in the accompanying proof.
    assert Y<F(1,10**10)
    assert Z1<F(4,5)
    assert Z2<F(60000)
    r=F(1,10**7)
    assert Y+(Z1+Z2*r)*r<r
    assert Z1+Z2*r<1
    print('EXACT FOURIER CERTIFICATE VERIFIED',flush=True)
    for name,q in [('omega',omega),('Y',Y),('Z1',Z1),('Z2',Z2),('radius',r),('finite_neumann_bound',neumann)]:
        print(name,'approximately',float(q),flush=True)
    print('Exact rational upper bounds: Y<1e-10, Z1<4/5, Z2<60000.',flush=True)
    result={name:str(q) for name,q in [('omega',omega),('Y',Y),('Z1',Z1),('Z2',Z2),('radius',r),('finite_neumann_bound',neumann)]}
    result['B']=[[str(v) for v in row] for row in B];result['tail']=[str(v) for v in tau]
    Path(__file__).with_name('fourier_bounds.json').write_text(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    if not __debug__:raise RuntimeError('Do not run this verifier with Python -O.')
    certify(method='python' if '--python' in sys.argv else 'int64')
