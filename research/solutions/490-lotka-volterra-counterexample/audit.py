import sys,numpy as np
from pathlib import Path
from fourier import AINT,complex_parts,exact_jacobian,exact_matmul,exact_residual
z=np.load(Path(__file__).with_name('fourier_certificate.npz'));M=48;N=128;H=N+M;Q=2**46;ints=z['coeffints'];R=z['Rints'];n=1+4*(2*N+1)
J,_,_=exact_jacobian(AINT,ints,Q,M,N,M)
cr,ci=complex_parts(ints,M);cr=cr.astype(object);ci=ci.astype(object)
yr=np.concatenate([cr[:,1:][:,::-1],cr],axis=1);yi=np.concatenate([-ci[:,1:][:,::-1],ci],axis=1)
a=AINT.astype(object);ayr=a@yr;ayi=a@yi
rng=np.random.default_rng(490)
for trial in range(5):
 hr=rng.integers(-3,4,size=(4,H+1)).astype(object);hi=rng.integers(-3,4,size=(4,H+1)).astype(object);hi[:,0]=0
 er=np.concatenate([hr[:,1:][:,::-1],hr],axis=1);ei=np.concatenate([-hi[:,1:][:,::-1],hi],axis=1)
 ar=a@er;ai=a@ei;om=int(rng.integers(-3,4));hv=np.zeros(n+8*M,dtype=object);hv[0]=om
 direct=np.zeros(n,dtype=object);direct[0]=1000*Q*hi[0,1]
 for i in range(4):
  b=1+i*(2*N+1);hv[b]=hr[i,0]
  for k in range(1,H+1):
   col=b+2*k-1 if k<=N else n+2*i*M+2*(k-N)-2
   hv[col]=hr[i,k];hv[col+1]=hi[i,k]
  # Derivative of y_i(A y)_i, evaluated independently using four convolutions.
  dr=np.convolve(yr[i],ar[i])-np.convolve(yi[i],ai[i])+np.convolve(er[i],ayr[i])-np.convolve(ei[i],ayi[i])
  di=np.convolve(yr[i],ai[i])+np.convolve(yi[i],ar[i])+np.convolve(er[i],ayi[i])+np.convolve(ei[i],ayr[i])
  for k in range(N+1):
   rr=-1000*k*int(ints[0])*hi[i,k]-Q*ar[i,H+k]-dr[M+H+k]
   ii= 1000*k*int(ints[0])*hr[i,k]-Q*ai[i,H+k]-di[M+H+k]
   if k<=M:rr-=1000*k*om*ci[i,k];ii+=1000*k*om*cr[i,k]
   if k==0:direct[b]=rr;assert ii==0
   else:direct[b+2*k-1]=rr;direct[b+2*k]=ii
 assert np.array_equal(J.astype(object)@hv,direct)
print('PASS: 5 exact full-convolution Jacobian checks, including tail inputs.')
# Direct Python-integer scalar products independently check accelerated products.
ri=rng.integers(0,n,size=9);cj=rng.integers(0,J.shape[1],size=11)
small=exact_matmul(R[ri,:],J[:,cj],progress=False)
truth=R[ri,:].astype(object)@J[:,cj].astype(object)
assert np.array_equal(small,truth)
print('PASS: 99 independent Python-integer checks of digit matrix products.')
# Anchor data.
print('omega integer',int(ints[0]),'denominator',Q)
for i in range(4):
 xnum=Q+int(cr[i,0])+2*sum(int(t) for t in cr[i,1:])
 print('anchor x(0)',i+1,xnum,'/',Q,'=',xnum/Q)
