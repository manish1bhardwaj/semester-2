# Write the program for addition of matrix

class array:
    def __init__(self,lst):
        self.lst = lst
    def reshape(self,m,n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
        self.lst = M
    def __add__(self,other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0]*c]*r))
        for i in range (r):
            for j in range(c):
                M[i][j] = self.lst[i][j] + other.lst[i][j]
            return array(M)    
    def disp_matrix(self):
        for i in self.lst:
            print(*i)       
        

#raw array
lst1 = list(map(int,input().split()))
r1,c1 = list(map(int,input().split()))
arr1 = array(lst1)
arr1.reshape(r1,c1)


lst2 = list(map(int,input().split()))
r2,c2 = list(map(int,input().split()))
arr2 = array(lst2)
arr2.reshape(r2,c2)

print('Matrix 1')
arr1.disp