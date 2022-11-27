Tamil=input("Enter your tamil mark: ")
English=input("Enter your English mark: ")
Maths=input("Enter your Maths mark: ")
Science=input("Enter your Science mark: ")
Social_science=input("Enter your social Science mark: ")
total_mark=int(Tamil)+int(English)+int(Maths)+int(Science)+int(Social_science)
print("total mark is: ",total_mark)
average= int(total_mark)/5

print("Average is : ",average)
# grade calculation
if(average>90):
    print("A grade")
elif(average>80):
    print("B grade")
elif(average>70):
    print("C grade")
else:
    print("fail")