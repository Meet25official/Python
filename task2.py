# Check if person is eligible for DL.

print("ANS 1:\n")

age = int(input("enter age: "))
if age>=18:
    print("Eligible.")
else:
    print("Not Eligible.")

print("\n")

# Check whether number is even or odd.

print("ANS 2:\n")

num = int(input("enter the number: "))
if num%2==0:
    print("Number is even.")
else:
    print("Number is odd.")

print("\n")

# Check number is divisible by 7 or not

print("ANS 3:\n")

num = int(input("Enter number :"))
if num%7==0:
    print("The num",num,"is divisible by 7.")
else:
    print("The num",num,"is not divisible by 7.")

print("\n")

# 1) WAP for a party in which 
# if dress code is “western dress” then it is western      party
# if dress code is “traditional dress” then it is traditional party
# if dresscode is “formals” then it is office party
# if dresscode is any other dress or no dress code then it is casual party.

print("ANS 4:\n")

dress = str(input("Enter dress name (western / tredition / formals):"))
if dress =="western":
    print("The party is a western party")
elif dress =="tredition":
    print("The party is a treditional party")
elif dress =="formals":
    print("The party is a office party")
else:
    print("TThe party is a casual party")

print("\n")

# 2) Traffic light code

print("ANS 5:\n")

light = str(input("Enter light :"))
if light=="red":
    print("stop")
elif light=="green":
    print("go")
elif light=="yellow":
    print("wait")
else:
    print("Not Light")

print("\n")

# Students marks with Grade
#     if marks> 90 then A+
#     if marks>75 and <90 then A
#     if marks>60 and <75 then B
#     if marks< 60 then C

print("ANS 6:\n")

marks = int(input("Enter the Marks: "))

if marks>=90:
    print("A+ Grade.")
elif marks>=75 and marks<90:
    print("A Grade.")
elif marks>=60 and marks<75:
    print("B Grade.")
elif marks<60:
    print("C Grade.")
else:
    print("Invelid Marks")

print("\n")

# WAP for quality checking (QC) and student (stu) (Boy/Girl) in which
#    if QC=1 or 2 & stu= B say “Good”
#    if QC=3 or 4 & stu= G say “Need improvement”
#    if QC=4 and stu= G say “Fair”
#    in any other QC say “Bad”

print("ANS 7:")
QC = int(input("Enter quality check (1-4): "))
stu = input("Enter student gender (B/G): ")

if (QC == 1 or QC == 2) and stu == 'B':
    print("Good")
elif (QC == 3 or QC == 4) and stu == 'G':
    if QC == 4:
        print("Fair")
    else:
        print("Need improvement")
    
else:
    print("Bad")

"""
ANS 1:

enter age: 21
Eligible.


ANS 2:

enter the number: 20
Number is even.


ANS 3:

Enter number :15
The num 15 is not divisible by 7.


ANS 4:

Enter dress name (western / tredition / formals):western
The party is a western party


ANS 5:

Enter light :red
stop


ANS 6:

Enter the Marks: 86
A Grade.


ANS 7:
Enter quality check (1-4): 2
Enter student gender (B/G): G
Good

"""