def qua_equ(a,b,c):
    if a != 0:
        d = (b**2) - (4*a*c)
        x_1 = (-b + d**0.5)/(2*a)
        x_2 = (-b - d**0.5)/(2*a)
    else :
        x_1 = -c/b
        x_2 = -1
    if x_1 >= 0 and x_2 < 0:
        print("Time Taken =",x_1,"s")
    elif x_2 >= 0 and x_1 < 0:
        print("Time Taken =",x_2,"s")
    elif x_1 >= 0 and x_2 >= 0:
        print("Time Taken =",x_1,"s", "or ", x_2, "s")
    return x_1, x_2

def equ_1(v=None, u=None, a=None, t=None):
    if v is None:
        v = u + (a*t)
        print("Final Velocity =",v,"m/s")
        return v
    elif u is None:
        u = v - (a*t)
        print("Initial Velocity =",u,"m/s")
        return u
    elif a is None:
        a = (v - u)/t
        print("Acceleration =",a,"m/s^2")
        return a
    elif t is None:
        t = (v - u)/a
        if t >= 0:
            print("Time Taken =",t,"s")
            return t
        else:
            print("Not Possible Because Time Cannot Be Negative!!")

def equ_2(s=None, u=None, a=None, t=None):
    if s is None:
        s = (u*t) + 0.5*(a*t*t)
        print("Displacement =", s, "m")
        return s
    elif u is None:
        u = (s - 0.5*(a*t*t))/t
        print("Initial Velocity =", u, "m/s")
        return u
    elif a is None:
        a = (s - (u*t))/t*t*2
        print("Acceleration =", a, "m/s^2")
        return a
    elif t is None:
        qua_equ(0.5*a,u,-s)
        return t

def equ_3(v=None, u=None, a=None, s=None):
    if v is None:
        v = ((u*u) + (2*a*s))**0.5
        print("Final Velocity =",v,"m/s")
        return v
    elif u is None:
        u = ((v*v) - (2*a*s))**0.5
        print("Initial Velocity =",u,"m/s")
        return u
    elif a is None:
        a = (v**2 - u**2)/2*s
        print("Acceleration =",a,"m/s^2")
        return a
    elif s is None:
        s = (v**2 - u**2)/(2*a)
        print("Displacement =",s,"m")
        return s

print("\t\t-----------------------------------")
print("\t\t--:PROGRAMMED BY RAMAN SHUKLA:--")
print("\t\t-----------------------------------")
print("This is the program based on three equations of motion:")
print("1. v = u + at")
print("2. s = ut + 1/2at^2")
print("3. v^2 = u^2 + 2as")
print("Enter The given values and Enter '*' in the finding value"
      " and Enter '#' in the not given value")
v = str(input("Enter The Final Velocity:"))
u = str(input("Enter The Initial Velocity:"))
a = str(input("Enter The Acceleration:"))
s = str(input("Enter The Displacement:"))
t = str(input("Enter The Time:"))

if v == '*':
    v = None
    if u != '#':
        u = float(u)
    if a != '#':
        a = float(a)
    if t != '#':
        t = float(t)
    if s != '#':
        s = float(s)
elif u == '*':
    u = None
    if v != '#':
        v = float(v)
    if a != '#':
        a = float(a)
    if t != '#':
        t = float(t)
    if s != '#':
        s = float(s)
elif a == '*':
    a = None
    if u != '#':
        u = float(u)
    if v != '#':
        v = float(v)
    if t != '#':
        t = float(t)
    if s != '#':
        s = float(s)
elif t == '*':
    t = None
    if u != '#':
        u = float(u)
    if a != '#':
        a = float(a)
    if v != '#':
        v = float(v)
    if s != '#':
        s = float(s)
elif s == '*':
    s = None
    if u != '#':
        u = float(u)
    if a != '#':
        a = float(a)
    if v != '#':
        v = float(v)
    if t != '#':
        t = float(t)

if v ==None and u!= None and a!= None and t!= None and v != '#' and u!= '#' and a!= '#' and t!='#':
    equ_1(v, u, a, t)
elif v !=None and u == None and a!= None and t!= None and v != '#' and u!= '#' and a!= '#' and t!='#':
    equ_1(v, u, a, t)
elif v !=None and u!= None and a == None and t!= None and v != '#' and u!= '#' and a!= '#' and t!='#':
    equ_1(v, u, a, t)
elif v !=None and u!= None and a!= None and t == None and v != '#' and u!= '#' and a!= '#' and t!='#':
    equ_1(v, u, a, t)


elif s ==None and u != None and a!= None and t!= None and s != '#' and u!= '#' and a!= '#' and t!='#':
    equ_2(s, u, a, t)
elif s !=None and u == None and a!= None and t!= None and s != '#' and u!= '#' and a!= '#' and t!='#':
    equ_2(s, u, a, t)
elif s !=None and u!= None and a == None and t!= None and s != '#' and u!= '#' and a!= '#' and t!='#':
    equ_2(s, u, a, t)
elif s !=None and u!= None and a!= None and t == None and s != '#' and u!= '#' and a!= '#' and t!='#':
    equ_2(s, u, a, t)


elif v ==None and u != None and a!= None and s!= None and v != '#' and u!= '#' and a!= '#' and s!='#':
    equ_3(v, u, a, s)
elif v !=None and u == None and a!= None and s!= None and v != '#' and u!= '#' and a!= '#' and s!='#':
    equ_3(v, u, a, s)
elif v !=None and u!= None and a == None and s!= None and v != '#' and u!= '#' and a!= '#' and s!='#':
    equ_3(v, u, a, s)
elif v !=None and u!= None and a!= None and s == None and v != '#' and u!= '#' and a!= '#' and s!='#':
    equ_3(v, u, a, s)
z = input()
