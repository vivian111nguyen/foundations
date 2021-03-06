

def mergeSort(arr):
    
    if len(arr) > 1: #need this if statement because the halving should stop after
    #L & R get too small. to not halve empty arrays forever
    
        m = len(arr)//2 #middle index
        L = arr[:m]
        R = arr[m:]
        
        mergeSort(L)
        mergeSort(R)
        
        l = r = k = 0
        
        while l < len(L) and r < len(R):
            
            if L[l] < R[r]:
                arr[k] = L[l]
                l += 1
                
            else:
                arr[k] = R[r]
                r += 1
            k += 1
              
        while l < len(L):
            
            arr[k] = L[l]
            l += 1
            k += 1
            
        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1
            
        print(arr)
        
arr = [2,5,3,1,3]

mergeSort(arr)

print(arr)

