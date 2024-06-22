import numpy as np

A = np.array([[1,4],[2,3]])

lamda1 = -1
lamda2 = 5

v1 = np.array([[-2],[1]])
v2 = np.array([[1],[1]])
def Av1(A,v1):
    print("Av1 = ")
    print(A@v1)
    print()
    return A@v1

def lamda1v1(lamda1,v1):
    print("λ1v1 = ")
    print(lamda1*v1)
    print()
    return lamda1*v1

def Av2(A,v2):
    print("Av2 = ")
    print(A@v2)
    print()
    return Av2

def lamda2v2(lamda1,v2):
    print("λ2v2 = ")
    print(lamda2*v2)
    print()
    return lamda2*v2

def eigenSum(lamda1,lamda2):
    print("固有値の和:",end="")
    print(lamda1+lamda2)
    print()
    return lamda1+lamda2

def trace(A):
    print("Aのトレース:",end="")
    print(np.trace(A))
    print()
    return np.trace(A)

def eigenMult(lamda1,lamda2):
    print("固有値の積:",end="")
    print(lamda1*lamda2)
    print()
    return lamda1*lamda2

def det(A):
    print("Aの行列式:",end="")
    print(np.linalg.det(A))
    return np.linalg.det(A)
