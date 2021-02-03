#Merge Sort
import time
import random

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0
    j = 0
    k = l
  
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
            k += 1
  
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
   
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)

def bestcase():
    arr = []

    for i in range(1000):
        arr.append(i)
        
    n = len(arr)
    
    begin = time.time()
    
    mergeSort(arr,0,n-1)
    
    end = time.time()

    print('Best Case Scenerio :' , end-begin)

def averagecase():
    arr = random.sample(range(0,1000),1000)
    
    n = len(arr)

    begin = time.time()
    
    mergeSort(arr,0,n-1)
    
    end = time.time()

    print('Average Case Scenerio :' , end-begin)
    
def worstcase():
    arr = []
    
    for i in range(1000):
        arr.append(1000-i)
        
    n = len(arr)
        
    begin = time.time()
    
    mergeSort(arr,0,n-1)
    
    end = time.time()

    print('Worst Case Scenerio :' , end-begin)

bestcase()
averagecase()
worstcase()
