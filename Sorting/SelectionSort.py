#Selection Sort
import time
import random

def bestcase():
    arr = []

    for i in range(1000):
        arr.append(i)
    
    begin = time.time()
    
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    end = time.time()

    print('Best Case Scenerio :' , end-begin)
    
def averagecase():
    arr = random.sample(range(0,1000),1000)

    begin = time.time()
    
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    end = time.time()

    print('Average Case Scenerio :' , end-begin)
    
def worstcase():
    arr = []
    
    for i in range(1000):
        arr.append(1000-i)
        
    begin = time.time()
    
    for i in range(len(arr)): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
              
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    end = time.time()

    print('Worst Case Scenerio :' , end-begin)

bestcase()
averagecase()
worstcase()
