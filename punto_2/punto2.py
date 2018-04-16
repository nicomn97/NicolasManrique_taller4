import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img=np.asarray(mpimg.imread("forest.png"))
print img.shape


def f2d(mat):
    tam=np.shape(mat)
    tran=np.zeros(tam,dtype=complex)
    N=tam[0]
    M=tam[1]
    for k in range(tam[2]):
        z=np.exp(-2.0j*np.pi*mat[:,:,k])
        for l in range(N):
            for m in range(M):
                zi=np.zeros(N,dtype=complex)
                for i in range(N):
                    zj=np.zeros(M,dtype=complex)
                    for j in range(M):
                        zj[j]=z[i,j]**((((1.0+(i*l)))/N)+(((1.0+(j*m)/M))))*mat[i,j,k]
                    zi[i]=np.sum(zj)
                tran[l,m,k]=np.sum(zi)
    for s in range(tam[2]):
        tran[:,:,s]=(1.0/(2.0*np.pi)*tran[:,:,s])
    return tran

def finv2d(mat):
    tam=np.shape(mat)
    tran=np.zeros(tam,dtype=complex)
    N=tam[0]
    M=tam[1]
    for k in range(tam[2]):
        z=np.exp(-2.0j*np.pi*mat[:,:,k])
        for l in range(N):
            for m in range(M):
                zi=np.zeros(N,dtype=complex)
                for i in range(N):
                    zj=np.zeros(M,dtype=complex)
                    for j in range(M):
                        zj[j]=z[i,j]**(((-(1.0+(i*l)))/N)-(((1.0+(j*m)/M))))*mat[i,j,k]
                    zi[i]=np.sum(zj)
                tran[l,m,k]=np.sum(zi)
    for s in range(tam[2]):
        tran[:,:,s]=((2.0*np.pi/(N*M))*tran[:,:,s])
    return tran


fim = f2d(img)
res = np.real(finv2d(fim))
print res


mpimg.imsave("suave.png", res)


