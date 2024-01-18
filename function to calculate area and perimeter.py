def Area_of_rectangle (l, b):
    return l*b
def perimeter_of_rectangle(l , b):
    return 2*(l+b)
        
#main code        
l = int(input())
b = int(input())

area= Area_of_rectangle (l, b)
perimeter= perimeter_of_rectangle(l , b)
print(f'Area of rectangle {area}')
print(f'perimeter of rectangle {perimeter}')