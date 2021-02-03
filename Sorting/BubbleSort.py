#Bubble Sort
import time
import random

def bestcase():
    arr = []

    for i in range(1000):
        arr.append(i)
        
    n = len(arr)
    
    begin = time.time()
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    end = time.time()

    print('Best Case Scenerio :' , end-begin)

def averagecase():
    arr = random.sample(range(0,1000),1000)
    n = len(arr)

    begin = time.time()
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    end = time.time()

    print('Average Case Scenerio :' , end-begin)
    
def worstcase():
    arr = []
    
    for i in range(1000):
        arr.append(1000-i)
        
    n = len(arr)
        
    begin = time.time()
    
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    end = time.time()

    print('Worst Case Scenerio :' , end-begin)

bestcase()
averagecase()
worstcase()
