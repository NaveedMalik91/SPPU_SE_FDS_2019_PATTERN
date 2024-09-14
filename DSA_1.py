
# Function for removing duplicate items enterred

def Remove(list1):
    list = []
    for val in list1:
        if val not in list:
            list.append(val)
    return list


"<----------------------------------------------->"
# Function for union of elements enterred


def union(list1, list2):
    list3 = list1.copy()
    for val in list2:
        if val not in list3:
            list3.append(val)
    return list3


"<---------------------------------------------->"
# Function for intersection of elements enterred


def intersection(list1, list2):
    list3 = list1.copy()
    for val in list2:
        if val in list3:
            list3.append(val)
    return list3


"<--------------------------------------------->"
# Function for difference of elements enterred


def difference(list1, list2):
    list3 = []
    for val in list1:
        if val not in list2:
            list3.append(val)
    return list3


"<------------------------------------------->"
# Function for symmetric difference


def symmetric(list1, list2):
    list3 = []
    S1 = difference(list1, list2)
    print("The difference of elements between list1 and list2 is:", S1)
    S2 = difference(list2, list1)
    print("The difference of elements between list2 and list1 is:", S2)

    list3 = union(S1, S2)
    return list3


"<--------------------------------------------------------->"
# Function for finding Number of students who play both Football and Badminton


def Cricket_Badminton(list1, list2):
    list3 = intersection(list1, list2)
    print("The List of students who play both Football and Badminton are:", list3)
    return len(list3)


"<---------------------------------------------------------->"
# Function for finding Number of students who play eitherCricket or Badminton but not both


def Either_Cric_or_Bad(list1, list2):
    list3 = symmetric(list1, list2)
    print("The List of students who play eitherCricket or Badminton but not both are:", list3)
    return len(list3)


"<----------------------------------------------------------->"
# Function for finding Number of students who play  neither  Cricket nor Badminton


def neithr_cric_nor_Bad(list1, list2, list3):
    list4 = difference(list1, union(list2, list3))
    print("The List of students who play neither Cricket nor Badminton are:", list4)
    return len(list4)


"<------------------------------------------------------------->"
# Function for finding Number of students who play  Cricket and Badminton but not football


def Cric_Bad_not_football(lst1, lst2, lst3):
    lst4 = difference(intersection(lst1, lst2), lst3)
    print("List of students who play cricket and football but not badminton is : ", lst4)
    return len(lst4)


"<----------------------------------------------------------------->"
# Main Function

# SE computer students list
SE_comp = []
num = int(input("Enter the total number of students\n"))
print("Enter the roll_no. of students")

for i in range(0, num):  # i repesents the number in range 0-num
    ele = input()  # this input is to take user enterred roll no
    SE_comp.append(ele)
print("Original list of roll no of students of SE_Comp :", (SE_comp))
SE_comp = Remove(SE_comp)
print("List of roll no of students of SE_Comp after removing Duplicates is :\n", (SE_comp))
print(" ")


"<----------------------------------------------------------------------->"

# List of cricket students
Cricket = []
num = int(input("Enter the  number of students who play cricket\n"))

print("Enter the roll_no. of students")
for i in range(0, num):  # i repesents the number in range 0-num
    ele = input()  # this input is to store user enterred roll no
    Cricket.append(ele)
print("Original list of roll no of students of SE_Comp who plays Cricket :", (Cricket))
Cricket = Remove(Cricket)
print("List of roll no of students of SE_Comp after removing Duplicates is :", (Cricket))
print(" ")


"<----------------------------------------------------------------------->"

# List of Badminton students
Badminton = []
num = int(input("Enter the  number of students who play Badminton\n"))

print("Enter the roll_no. of students")
for i in range(0, num):  # i repesents the number in range 0-num
    ele = input()  # this input is to store user enterred roll no
    Badminton.append(ele)
print("Original list of roll no of students of SE_Comp who plays Badminton:", (Badminton))
Badminton = Remove(Badminton)
print("List of roll no of students  after removing Duplicates is :", (Badminton))
print(" ")


"<------------------------------------------------------------------------>"

# List of Football students
Football = []
num = int(input("Enter the  number of students who play Football\n"))

print("Enter the roll_no. of students")
for i in range(0, num):  # i repesents the number in range 0-num
    ele = input()  # this input is to store user enterred roll no
    Football.append(ele)
print("Original list of roll no of students of SE_Comp who plays Football :", (Football))
Football = Remove(Football)
print("List of roll no of students of SE_Comp after removing Duplicates is :", (Football))
print(" ")


"<-------------------------------------------------------------------->"
flag = 1
while flag == 1:
    print("\n\n--------------------Choice--------------------\n")
    print("1. List of students who play both cricket and badminton")
    print("2. List of students who play either cricket or badminton but not both")
    print("3. List of students who play neither cricket nor badminton")
    print("4. Number of students who play cricket and football but not badminton")
    print("5. Exit\n")

    choice = int(input("Enter your choice\n"))

    if (choice == 1):

        # passing actual argumnets as cric and bad lists instead od formal arguments i.e list1 and list2
        print("Number of students who play both cricket and badminton : ",Cricket_Badminton(Cricket, Badminton))

    elif (choice == 2):
        print("List of students who play either cricket or badminton but not both are: ",
              Either_Cric_or_Bad(Cricket, Badminton))

    elif (choice == 3):
        print("List of students who play neither cricket nor badminton are: ", neithr_cric_nor_Bad(SE_comp, Cricket, Badminton))   # SE_COMP USED AS UNIVERSAL SET

    elif (choice == 4):
        print("List of students who play cricket and  badminton but not Football are:",Cric_Bad_not_football(Cricket, Badminton, Football))

    elif (choice == 5):
        flag = 0
        print("Thanks for using this program!")
        break
