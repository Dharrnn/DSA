arr1 = ['a','b','c','d']
arr2 = ['x','y',]

def substring(arr1,arr2):
    h1 = set()
    for i in range(len(arr1)):
        h1.add(arr1[i])
    for i in arr2:
        if i in h1:
            return(True)
    return(False) 

print(substring(arr1,arr2))