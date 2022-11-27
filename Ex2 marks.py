Eng=input("Enter the english mark: ")
mat=input("Enter the maths mark: ")
phy=input("Enter the physics mark: ")

if(int(Eng)>=75  and int (mat)>=75):
    print("pass")
    print("English and Maths mark is: ",Eng,mat)
elif(int(mat)>=75 and int(phy)>=75):
    print("pass")
    print("Maths and physics mark is: ",mat,phy)
elif(int(phy)>=75 and int(phy)>=75):
    print("pass")
    print("physics and English mark is : ",phy,Eng)
elif(int(Eng)>=60 and int(mat)>=60 and int(phy)>=60):
    print("pass")
    print("Eglish and maths and physics mark is: ",Eng,mat,phy)
else:
    print("fail")