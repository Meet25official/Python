# WAP to store grades of 10 students in a list and sort it in ascending order and descending order.

grades = [90, 85, 88, 75, 60, 92, 77, 81, 79, 95]

ascending_order = sorted(grades)
print("Grades in Ascending Order:", ascending_order)

descending_order = sorted(grades, reverse=True)
print("Grades in Descending Order:", descending_order)


# WAP to input three of your friend’s name and store them in a list.

friend1 = input("Enter the name of your first friend: ")
friend2 = input("Enter the name of your second friend: ")
friend3 = input("Enter the name of your third friend: ")

friends_list = [friend1, friend2, friend3]

print("Your friends' names are:", friends_list)

# WAP to check if given list is palindrome or not.

list = [1,2,3,2,1]
list1 = list.copy()

list1.reverse()
if list==list1:
    print("The given list is a palindrome.")
else:
    print("The given list is not a palindrome.")

# WAP to swap first and last element of list.
# WAP to swap any two elements in a list.

list = ['a','b','c','d']
list[0],list[3] = list[3],list[0] 
print(list)

# WAP to check if element exists in list.

list = ["a","b","c","d"]
i="c"
if i in list:
    print("element exists")
else:
    print("element not exists")

# WAP to copy a list without using copy( ) hint: slicing , append.

original_list = [1, 2, 3, 4, 5]

copied_list = original_list[:]

print("Original List:", original_list)
print("Copied List:", copied_list)

# WAP to find the sum and average of list.

L = [4, 5, 1, 2, 9, 7, 10, 8]
count = sum(L)
avg = count / len(L)
print(f"Sum: {count}, Average: {avg:.2f}")

# WAP to check if list is empty or not.

my_list = [1,2,3]
if my_list == []:
    print("The list is empty.")
else:
    print("The list is not empty.")

# WAP to count number of students with “A” grade in a tuple.( A,B,C,C,B,C,A,A,B,D,A)

list = ("a","b","c","c","b","c","a","a","b","d","a")
count = list.count("a")
print(count)

# WAP to store following in a dictionary.
#    table = piece of furniture, number   multiplication
#    cat = animal

dict = {
    "table" : ("piece of furniture" , "number   multiplication"),
    "cat":"animal"
}
print(dict)

# WAP to input 3 subject’s marks from user and store them in dictionary. Start with empty dictionary and add one by one.

markmarks_dict = {}

subject1 = input("Enter subject 1 name: ")
marks1 = float(input("Enter marks for {}: ".format(subject1)))
marks_dict[subject1] = marks1

subject2 = input("Enter subject 2 name: ")
marks2 = float(input("Enter marks for {}: ".format(subject2)))
marks_dict[subject2] = marks2

subject3 = input("Enter subject 3 name: ")
marks3 = float(input("Enter marks for {}: ".format(subject3)))
marks_dict[subject3] = marks3

print("Subject-wise marks:", marks_dict)