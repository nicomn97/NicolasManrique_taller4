import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = np.linspace(0,6.5,1000)

def f2d(mat):
    N=np.shape(mat)[0]
    z=np.exp(-2.0j*np.pi*mat)
    tran=np.zeros(N,dtype=complex)
    for l in range(N):
        zi=np.zeros(N,dtype=complex)
        for i in range(N):
            zi[i]=(z[i]**((i*(l+1.0))/N))*mat[i]
        tran[l]=np.sum(zi)
    tran=(tran/(np.sqrt(2.0*np.pi)))
    return tran


def finv2d(mat):
    N=np.shape(mat)[0]
    z=np.exp(-2.0j*np.pi*mat)
    tran=np.zeros(N,dtype=complex)
    for l in range(N):
        zi=np.zeros(N,dtype=complex)
        for i in range(N):
            zi[i]=(z[i]**(-(i*(l+1.0))/N))*mat[i]
        tran[l]=np.sum(zi)
    tran=(tran*np.sqrt(2.0*np.pi)/N)
    return tran



fim = f2d(img)
res = np.real(finv2d(fim))

print res




