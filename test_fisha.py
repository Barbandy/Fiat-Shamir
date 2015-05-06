#coding: UTF-8
import random, pytest, fisha, BigInt

def test_fisha():
    y, yy = fisha.main()
    
    assert y == yy