'''
  1、定义变量符号
  2、定义函数：+、-、*、/、**、log、exp、sqrt、root、……
  3、代入x的数值
'''
'''import sympy
from sympy import *
x=Symbol('x')       #初始化符号
y=Symbol('y')
f=x**2+y**2+x/2         #初始化函数f(x)
g=sympy.log(x)+sympy.sqrt(x)+sympy.root(y,3)+sympy.exp(y)
h=sympy.factorial(4)+sympy.sin(sympy.pi/3)
print(" f=",f,"\t","g=",g,"\t","h= sin(π/3) + 4! =",h)
f_x=f.evalf(subs={x:2})     #代入数值
print("x=2时,f =",f_x)'''

'''import sympy as sy
from sympy import *
x=sy.Symbol('x')
z,y=sy.symbols("z,y")
F=sy.Function('F')
f=sy.sin(x)+sy.cos(x)-1
g=5*y+3*z-2
h=6*y-5*z+1
eq1 = F(x).diff(x,1)-2*x*F(x)
eq2 = F(x)**2+x**2*F(x).diff(x,1)-x*F(x)*F(x).diff(x,1)
print("1、显函数方程，例如：sin(x) + cos(x) = 1，解得：x =",sy.solve(f,x))
print("  再例如 x**2 + x + 1 =0，解得：x =",sy.solve(x**2 + x + 1,x))
print("\t 若需要指定值范围，可使用solveset，例如sy.solveset(x**2 + x - 1,x,Interval(0, 50))，得：",sy.solveset(x**2 + x - 1,x,Interval(0, 50)))
print("\t 简单的隐函数解方程也可实现，例如 y**2+z**2=25，解得：",sy.solve(y**2+z**2-25,z,y))
print("2、显函数方程组，例如：5y+3z=2 & 6y-5z=-1 ，解得：",sy.solve([g,h],[y,z]))
print("3、微分方程，例如xy'-2x=y**3，通解为：",eq2,sy.dsolve(eq2,F(x)))  #垃圾，这个微分方程都解不出来，老子不干了
'''
'''import sympy as sy
from sympy import *

x,y,z,t=sy.symbols("x,y,z,t")
f=x**3+sy.sin(x**2)+sy.ln(x)
g=y**z+sy.csc(y*2)+sy.exp(z**3)
h=x**2+y**3-2
print("1、一元函数极限，例如f=e**-x，在x=oo处极限为：",limit(sy.exp(-x),x,0,dir='-'))
print("\t 多元函数极限，例如f=x**2+y**2-25，在x=0处极限为：",limit(x**2+y**2-25,x,0,dir="-"))
print("2、一元函数一阶导数，例如f=x**3+sin(x**2)+ln(x)，一阶导数为：f'(x) =",diff(f,x))
print("3、一元函数高阶导数，例如f=x**3+sin(x**2)+ln(x)，四阶导数为：f4(x) =",diff(f,x,4))
print("4、一元函数具体数值代入，例如f=x**3+sin(x**2)+ln(x)，x=1时一阶导数值为：",diff(f,x).subs(x,2))
print("5、多元函数偏微分，例如g=y**z+sy.csc(y*2)+sy.exp(z**3)，其偏y偏z为：",diff(g,y,1,z,1))
print("6、隐函数导数，例如h=x**2+y**3-2，其一阶导数为：h'(x) =",idiff(h,y,x))
print("7、参数方程导数，例如 x=cost*e**t & y=sint*e**t，其导数为：",diff(sy.cos(t)*sy.exp(t),t)/diff(sy.sin(t)*sy.exp(t),t))    #参数方程求导为y'/x'
print("8、泰勒展开，例如y=cosx在x=0的六阶展开为：",sy.cos(x).series(x,0,6))'''