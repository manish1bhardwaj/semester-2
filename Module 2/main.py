import numpy as np

# lst = [1,2,3]
# arr = np.array(lst,dtype = None,ndmin = 0)
# print(arr)

# lst = [[2,3,4], [5,6,7]]
# arr = np.array(lst)
# print(arr,arr.shape,arr.ndim)

# arr1 = np.array([2,3,4,5,6,7])
# arr2 = np.array([3,5,7,8,9,0])
# arr1.shape = (3,2)
# arr2.shape = (3,2)

# m1 = arr1.reshape((2,3))
# m2 = arr2.reshape((2,3))
# print(arr1)
# print(m2)

# m = np.multiply(m1,m2)
# print(m)



# arr = list(map(float,input().split()))
# arr1 = np.flip(arr)
# print(arr1)

# arr = list(map(float,input().split()))
# arr1 = np.array(arr).reshape(2,3)
# print(arr1)

m,n = list(map(int,input().split()))
arr1 = np.eye(m,n) 
print(arr1)
a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
m=list(map(int,input().split()))
arr1=np.array(l).reshape(a,b)
arr2=np.array(m).reshape(a,b)
arr  = np.multiply(arr1,arr2)
arr3 = np.add(arr1,arr2)
arr4 = np.subtract(arr1,arr2)
arr5 = np.floor_divide(arr1,arr2)
arr6 = np.mod(arr1,arr2)
arr7 = np.power(arr1,arr2)
print(arr5)
print(arr4)
print(arr3) 
print(arr)
print(arr6)
print(arr7)

