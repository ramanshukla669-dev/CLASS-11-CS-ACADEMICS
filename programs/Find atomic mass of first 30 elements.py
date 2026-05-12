print("-----------------PROGRAM TO KNOW ATOMIC MASS OF FIRST 30 ELEMENTS ---------------")
a=1
while (a>0):
    ele_nme=input("Enter the Name of the element: ")
    atm_no=int(input("Enter the 'ATOMIC NUMBER': "))
    L3=["Argon","Titanium","Chromium","Iron"] 
    L4=["Scandium","Nickel"] 
    L5=["Vanadium","Manganese","Cobalt","Copper","Zinc"] 
    evenorodd=atm_no%2
    if ele_nme=="hydrogen":
        print("The",ele_nme,"'s","ATOMIC MASS IS :","1")
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif ele_nme=="Beryllium":
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2+1)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif ele_nme=="Nitrogen":
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif ele_nme in L3:
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2+4)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif ele_nme in L4:
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2+3)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif ele_nme in L5:
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2+5)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif evenorodd==0:
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    elif evenorodd==1:
        print("The",ele_nme,"'s","ATOMIC MASS IS :", atm_no*2+1)
        print("----------------------------------------------------------------------------------------------------------------------------------")
    else:
        print("Enter the value of ATOMIC NUMBER only in 'integer form'")
        a+=1
