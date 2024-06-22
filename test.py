import pytest
import numpy as np
from kadai1 import Av1, Av2,lamda1v1,lamda2v2,eigenSum,eigenMult,trace,det
A = np.array([[1,4],[2,3]])

lamda1 = -1
lamda2 = 5

v1 = np.array([[-2],[1]])
v2 = np.array([[1],[1]])

class TestMyTask(unittest.TestCase):
    def Av1_lamda1v1(self):
        val1 = Av1(A,v1)
        val2 = lamda1v1(lamda1,v1)
        self.assertEqual(val1,val2)

    def TestSumTrace(self):
        val1 = eigenSum(lamda1,lamda2)
        val2 = trace(A)
        self.assertEqual(val1,val2)

    def TestMultDet(self):
        val1 = eigenMult(lamda1,lamda2)
        val2 = det(A)
        self.assertEqual(val1,val2)

if _name_ == "__main__":
    unittest.main()
