import pandas as pd
import numpy as np
import math

df=pd.read_csv("data2023.csv", index_col=0)

def dot(v1,v2):
    total=0
    for i in range(0,len(v1)):
        total+=v1[i]*v2[i]
    if total==0:
        return 0
    else:
        return total

def cosine(v1,v2):
    k=math.sqrt(dot(v1,v1)*dot(v2,v2))
    if dot(v1,v2)==0 or k==0:
        return 0
    else:
        return dot(v1,v2)/k


def work_that_CPU(num_iteration_cos):
    import random
    import multiprocessing
    #import time
    num_words=200
    number_of_documents=20
    cosine_dict_all={}
    time_dict_all={}
    for i in range(1,number_of_documents+1):
        for j in range(1,number_of_documents+1):
            if i!=j and j>i:
                first_df=df.iloc[:num_words,i-1:i]
                second_df=df.iloc[:num_words,j-1:j]
                array_first=first_df.values
                array_second=second_df.values
                for k in range(num_iteration_cos):
                    cos=cosine(array_first,array_second)
    print("{}%".format(i/20))

    
    
    
    
    