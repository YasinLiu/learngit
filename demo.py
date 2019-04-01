'''
    Author: Yasin Liu
    Content: <Data structures> chapter 1 
'''
import numpy as np
import os
import pandas as pd 

coefficient = 0.6

result = 0
def distance_sum(init_height, times):
    if times < 0:
        return 0
    else:
        times -= 1
        result = init_height + init_height*coefficient + distance_sum(init_height*coefficient, times)
        return result


if __name__ == '__main__':
    s = distance_sum(10, 2)
    print(s)