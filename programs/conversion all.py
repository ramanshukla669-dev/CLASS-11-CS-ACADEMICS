
print("choose one of them \n 1)binary to decimal\n 2)octal on decimal \n 3)hexadecimal to decimal \n 4)decimal to binary \n 5)decimal to octal \n 6)decimal to hexadecimal")
a1=int(input("= "))
print("how many digits are there in your no form 1-10")
a2=int(input())
 


c2=a2
c3=a2-1
c4=a2-2
c5=a2-3
c6=a2-4
c7=a2-5
c8=a2-6
c9=a2-7
c10=a2-8
c11=a2-9
c12=a2-10



 


    


if a1==1 or a1==2 or a1==3:      
 if a2==10: 
   if a1==1 or a1==2 or a1==3: 
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    b6=int(input("enter first digit= "))
    b7=int(input("enter first digit= "))
    b8=int(input("enter first digit= "))
    b9=int(input("enter first digit= "))
    b10=int(input("enter first digit= "))
    
   elif a2==9:
    
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    b6=int(input("enter first digit= "))
    b7=int(input("enter first digit= "))
    b8=int(input("enter first digit= "))
    b9=int(input("enter first digit= "))
    c9=b1,b2,b3,b4,b5,b6,b7,b8,b9
 elif a2==8:
    
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    b6=int(input("enter first digit= "))
    b7=int(input("enter first digit= "))
    b8=int(input("enter first digit= "))
    c8=b1,b2,b3,b4,b5,b6,b7,b8
    
 elif a2==7:
  
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    b6=int(input("enter first digit= "))
    b7=int(input("enter first digit= "))
    c7=b1,b2,b3,b4,b5,b6,b7
 elif a2==6:
    
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    b6=int(input("enter first digit= "))
    c6=b1,b2,b3,b4,b5,b6
 elif a2==5:
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    b5=int(input("enter first digit= "))
    c5=b1,b2,b3,b4,b5
 elif a2==4:
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    b4=int(input("enter first digit= "))
    c4=b1,b2,b3,b4
 elif a2==3:
    b1=int(input("enter first digit= "))
    b2=int(input("enter first digit= "))
    b3=int(input("enter first digit= "))
    c3=b1,b2,b3
 elif a2==2:
     b1=int(input("enter first digit= "))
     b2=int(input("enter first digit= "))
     c2=b1,b2
 elif a2==1:
    b1=int(input("enter first digit= "))
    c2=b1
 else:
    print("write no all together")
    x=int(intput)
elif a1==4 or a1==5 or a1==6:
    an=int(input("enter value"))
else :
   print("something went wrong try again later")


   
 









    
    

if a1==1:
    if a2==10:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6)+(b6*2**c7)+(b7*2**c8)+(b8*2**c9)+(b9*2**c10)+(b10*2**c11))/2
        print(c)
        print("b2d")
    elif a2==9:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6)+(b6*2**c7)+(b7*2**c8)+(b8*2**c9)+(b9*2**c10))/2
        print(c)
        print("b2d")
    elif a2==8:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6)+(b6*2**c7)+(b7*2**c8)+(b8*2**c9))/2
        print(c)
        print("b2d")
    elif a2==7:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6)+(b6*2**c7)+(b7*2**c8))/2
        print(c)
        print("b2d")
    elif a2==6:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6)+(b6*2**c7))/2
        print(c)
        print("b2d")
    elif a2==5:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5)+(b5*2**c6))/2
        print(c)
        print("b2d")
    elif a2==4:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4)+(b4*2**c5))/2
        print(c)
        print("b2d")
    elif a2==3:
        c=((b1*2**a2)+(b2*2**c3)+(b3*2**c4))/2
        print(c)
        print("b2d")
    elif a2==2:
        c=((b1*2**a2)+(b2*2**c3))/2
        print(c)
        print("b2d")
    elif a2==1:
        c=((b1*2**a2))/2
        print(c)
        print("b2d")
    else:
        print("something went wrong try again later")


elif a1==2:
    if a2==10:
        c=((b1**8*a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6)+(b6*8**c7)+(b7*8**c8)+(b8*8**c9)+(b9*8**c10)+(b10*8**c11))/8
        print(c)
        print("b2d")
    elif a2==9:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6)+(b6*8**c7)+(b7*8**c8)+(b8*8**c9)+(b9*8**c10))/8
        print(c)
        print("b2d")
    elif a2==8:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6)+(b6*8**c7)+(b7*8**c8)+(b8*8**c9))/8
        print(c)
        print("b2d")
    elif a2==7:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6)+(b6*8**c7)+(b7*8**c8))/8
        print(c)
        print("b2d")
    elif a2==6:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6)+(b6*8**c7))/8
        print(c)
        print("b2d")
    elif a2==5:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5)+(b5*8**c6))/8
        print(c)
        print("b2d")
    elif a2==4:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4)+(b4*8**c5))/8
        print(c)
        print("b2d")
    elif a2==3:
        c=((b1*8**a2)+(b2*8**c3)+(b3*8**c4))/8
        print(c)
        print("b2d")
    elif a2==2:
        c=((b1*8**a2)+(b2*8**c3))/8
        print(c)
        print("b2d")
    elif a2==1:
        c=((b1*8**a2))/8
        print(c)
        print("b2d")
    else:
        print("something went wrong try again later")
        print("o2d")
        
elif a1==3:
    print("a=10\n b=11\n c=12\n d=13\n e=14\n f=15\n")
    if a2==10:

        c=((b1**16*a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6)+(b6*16**c7)+(b7*16**c8)+(b8*16**c9)+(b9*16**c10)+(b10*16**c11))/16
        print(c)
        print("b2d")
    elif a2==9:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6)+(b6*16**c7)+(b7*16**c8)+(b8*16**c9)+(b9*16**c10))/16
        print(c)
        print("b2d")
    elif a2==8:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6)+(b6*16**c7)+(b7*16**c8)+(b8*16**c9))/16
        print(c)
        print("b2d")
    elif a2==7:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6)+(b6*16**c7)+(b7*16**c8))/16
        print(c)
        print("b2d")
    elif a2==6:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6)+(b6*16**c7))/16
        print(c)
        print("b2d")
    elif a2==5:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5)+(b5*16**c6))/16
        print(c)
        print("b2d")
    elif a2==4:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4)+(b4*16**c5))/16
        print(c)
        print("b2d")
    elif a2==3:
        c=((b1*16**a2)+(b2*16**c3)+(b3*16**c4))/16
        print(c)
        print("b2d")
    elif a2==2:
        c=((b1*16**a2)+(b2*16**c3))/16
        print(c)
        print("b2d")
    elif a2==1:
        c=((b1*16**a2))/16
        print(c)
        print("b2d")
    else:
        print("something went wrong try again later")
    
    print("h2d")

    

elif a1==4:
    L=[]
    final_value=0
    while(an !=0):
      temp=an%2
      L.append(temp)
      an=an//2

    L.reverse()
    print(L)
    print("d2b")
elif a1==5:
   L=[]
   final_value=0
   while(an !=0):
    temp=an%8
    L.append(temp)
    an=an//8
    
   L.reverse()
   print(L)
   print("d2o")
elif a1==6:
 print("d2h")
else:
    print("something went wrong try again later")
    
    
