import os,sys
sys.path.append(os.getcwd())
from nth_lefttruncatableprime import fun_nth_lefttruncatableprime
import pytest
# 2,3, 5, 7, 13, 17, 23, 37, 43, 47, 53, 67, 73, 83, 97, 103, 107, 113, 137, 167, 173, 197, 223, 283, 307...

@pytest.mark.parametrize('a, result',[
   (0,2),(1, 3),(5, 17),(10,53),
# (15,113),(20,223),(25,347),
(15,103),(20,173),(25,313),
])
def test_fun_nth_lefttruncatableprime(a, result):
    assert fun_nth_lefttruncatableprime(a) == result

