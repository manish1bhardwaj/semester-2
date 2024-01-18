def validity_array(ls,valid_type):
    return all ([valid_type == type(i) for i in ls])
#maincode
ls = [3, 4, 5, 6, 1.0, 8]
re =validity_array(ls,int)
print(re)