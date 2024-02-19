import math
print('请依次输入二次方程\"ax^2+bx+c\"的三个因数a、b、c')
a = int(input('请输入a: '))
b = int(input('请输入b: '))
c = int(input('请输入c: '))
def quadratic(a, b, c):
    q = b*b-4*a*c
    if q < 0:
        return '该方程无实根'
    elif q == 0:
        cc = -b/(2*a)
        return cc
    else:
        aa = (-b+math.sqrt(q))/(2*a)
        bb = (-b-math.sqrt(q))/(2*a)
    return (aa,bb)
print(quadratic(a,b,c))