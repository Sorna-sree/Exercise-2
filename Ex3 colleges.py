Tamil=input("Enter your tamil mark: ")
English=input("Enter your English mark: ")
Maths=input("Enter your Maths mark: ")
Science=input("Enter your Science mark: ")
Social_science=input("Enter your social Science mark: ")
total_mark=int(Tamil)+int(English)+int(Maths)+int(Science)+int(Social_science)
print("total mark is: ",total_mark)
average= int(total_mark)/5
print("average mark is: ",average)
#eligible of college
if(average>=90):
    print("You are eligible to PSG college of Technology")
elif(average>=80):
    print("you are eligible to Indian Institute of Technology")
elif(average>=60):
    print("you are eligible to Sethu Institute of Technology")