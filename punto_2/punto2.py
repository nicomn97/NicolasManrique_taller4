import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img=np.asarray(mpimg.imread("imagen.png"))  ##Guarda filtro alto y bajo para imagen.png
print img.shape


def f2d(mat):
    tam=np.shape(mat)
    tran=np.zeros(tam,dtype=complex)
    N=tam[0]-1
    M=tam[1]-1
    for k in range(tam[2]):
        z=np.exp(-2.0j*np.pi*mat[:,:,k])
        for l in range(N):
            for m in range(M):
                zi=np.zeros(N,dtype=complex)
                for i in range(N):
                    zj=np.zeros(M,dtype=complex)
                    for j in range(M):
                        zj[j]=(z[i,j]**((((i+1*l)/N)+((j+1*m)/M))))*mat[i,j,k]
                    zi[i]=np.sum(zj)
                tran[l,m,k]=np.sum(np.nan_to_num(zi))
        print 1*k
    for s in range(tam[2]):
        tran[:,:,s]=(1.0/(2.0*np.pi)*tran[:,:,s])
    return tran

def finv2d(mat):
    tam=np.shape(mat)
    tran=np.zeros(tam,dtype=complex)
    N=tam[0]-1
    M=tam[1]-1
    for k in range(tam[2]):
        z=np.exp(-2.0j*np.pi*mat[:,:,k])
        for l in range(N):
            for m in range(M):
                zi=np.zeros(N,dtype=complex)
                for i in range(N):
                    zj=np.zeros(M,dtype=complex)
                    for j in range(M):
                        zj[j]=(z[i,j]**((-((i+1*l)/N)-((j+1*m)/M))))*mat[i,j,k]
                    zi[i]=np.sum(np.nan_to_num(zj))
                tran[l,m,k]=np.sum(zi)
        print 7*k
    for s in range(tam[2]):
        tran[:,:,s]=(((2.0*np.pi/(N*M))*tran[:,:,s]))
    return tran

def norm(arr):
    s=np.shape(arr)
    arr=arr.real
    for i in range(s[2]):
        maxim=np.max(arr[:,:,i])
        minim=np.min(arr[:,:,i])
        arr[:,:,i]=((arr[:,:,i]-minim)/(maxim-minim))
    return arr

def alto(arr):
    s=np.shape(arr)
    arr=arr.real
    for i in range(s[2]):
        maxim=np.max(arr[:,:,i])
        minim=np.min(arr[:,:,i])
        arr[:,:,i]=((arr[:,:,i]-minim)/(maxim-minim))
    return arr

def bajo(arr):
    s=np.shape(arr)
    arr=arr.real
    for i in range(s[2]):
        maxim=np.max(arr[:,:,i])
        minim=np.min(arr[:,:,i])
        arr[:,:,i]=((arr[:,:,i]-minim)/(maxim-minim))
    return arr



fim = f2d(img)

alto = alto(fim)
bajo = bajo(fim)

res = finv2d(fim)
mpimg.imsave("altas.png", norm(alto))
mpimg.imsave("bajas.png", norm(bajo))




