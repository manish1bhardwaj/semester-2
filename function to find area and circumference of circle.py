def area_of_circle(r):
    return(3.14*r*r)
def circumference_of_circle(r):
    return(2*3.14*r)

#manin code
r =int(input())
area = area_of_circle(r*r)
circumference = circumference_of_circle(r)
print(f'area of circle {area}')
print(f'circumference of circle {circumference}')
