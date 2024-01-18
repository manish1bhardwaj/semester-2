def sorted_or_not(ls):
      tmp = ls.copy()
      tmp.sort()
      if tmp == ls:
            return 1
      elif tmp == ls[::-1]:
            return 0
      else:
            return -1

#maincode
ls = [1,2,3,4,5,6,7,8,]
re = sorted_or_not(ls)
print(re)