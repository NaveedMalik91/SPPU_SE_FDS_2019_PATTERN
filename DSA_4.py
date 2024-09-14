class Student:
    def __init__(self):
        self.num = 0
        self.students = []

#<-----------------------ARRAY TO STORE STUDENTS---------------------->       
    def arr_roll_no(self):
        self.num = int(input("Enter number of students\n"))
        while(self.num > 0 ):
            for i in range(self.num):
                roll_num = int(input(f"Enter the roll_numbers of students {i+1} :\n"))
                self.students.append(roll_num)
            print("The array of students = ",self.students)
            return self.students
        
#<-----------------------Function for Linear Search-------------------->
    def linear_search(self):
        print("The array of students =", self.students)
        search_rollno = int(input("\nEnter the roll you wish to search\n"))

        for i in range(self.num):
            if self.students[i] == search_rollno:
                print(f"The student roll_no = {search_rollno} has attended the training program")
                print(f"The student is present at index = {i}\n")
                break  # Exit the loop once the element is found
        else:
            print(f"The student, roll_no = {search_rollno} hasn't attended the training program")

 
#<-----------------------Function for Sentinel Search-------------------->
    def sentinel_search(self):
        n = len(self.students)
        print("The array of students =", self.students)
        search_rollno = int(input("\nEnter rollno you wish to search\n"))
        last_ele = self.students[n - 1]  # last value of array stored in this variable
        temp = last_ele  # Store the last value in temp
        search_rollno = last_ele  # Value to search is placed at the last index

        i = 0

        while self.students[i] != search_rollno:
            i += 1
        if (i < n - 1 and self.students[i] == search_rollno):
            print("The student has attended the training program")
            print(f"The student roll_no = {search_rollno} found at index = {i}")

        else:
            print(f"The student, rollno hasn't attended the training program")
        self.students[n - 1] = temp  # Restore the original value at the last index

    #<-----------------------Sorting Array of students-------------------->
    def sort_rollno(self):
        for i in range(len(self.students)):        #This will scan all the elements in array
            for j in range(i+1,len(self.students)):  #This will scan all elements from current iteration and compares with elements right to current index
                if(self.students[i] > self.students[j]):
                    temp = self.students[i]
                    self.students[i] = self.students[j]
                    self.students[j] = temp
        return self.students

  
    #<-----------------------Function for Binary Search-------------------->
    def Binary_search(self):
        n = len(self.students)
        sorted_rollno = self.sort_rollno()  # It will ensure that students array will be sorted one now
        print("\nThe sorted array of rollno of student =",sorted_rollno)
        search_rollno = int(input("Enter the rollno wish to search :\n"))
        strt_indx = 0     
        end_indx = n-1

        while(strt_indx <= end_indx):   #this will limit the searching interval
            mid = (strt_indx + end_indx)//2
            if self.students[mid] ==search_rollno:
                print("The Student has attended the training program")
                print(f"The student, rollno = {search_rollno} is present at index = {mid}")
                break
            elif self.students[mid] < search_rollno:   
                strt_indx  = mid + 1                        #shift towards right

            elif self.students[mid] > search_rollno:
                end_indx = mid - 1
        if strt_indx > end_indx:
            print(f"The student with roll no = {search_rollno} didn't attend the training program")
        return -1
    
    #<----------------------------------Fibonacchi Search---------------------------------->

    def fibonacchi_search(self):
        sorted_rollno = self.sort_rollno()  # Students array will be now sorted
        print("\nThe sorted array of rollno of student =", sorted_rollno)

        n = len(self.students)  # This will give the total number of elements in the array
        search_rollno = int(input("Enter the roll no you wish to search\n"))

    # Initialize Fibonacci numbers and generate fib_numbers
        fib_2 = 0  # (m-2)th
        fib_1 = 1  # (m-1)th
        fib_m = fib_1 + fib_2
        offset = -1  # Start from the beginning of the sorted array

        while fib_m <= n - 1:  # n-1 will give the last valid index
            fib_2 = fib_1
            fib_1 = fib_m
            fib_m = fib_2 + fib_1

        while fib_m > 1:
            i = min(offset + fib_2, n - 1)
            if self.students[i] == search_rollno:
                print("The student has attended the training program")
                print(f"The student, rollno = {search_rollno} is present at index = {i}")
                break

        # Move fib_m down by one and reset offset and fib_1 and fib_2 accordingly
            elif self.students[i] < search_rollno:
                fib_m = fib_1
                fib_1 = fib_2
                fib_2 = fib_m - fib_1
                offset = i

        # Move fib_m down by 2
            elif self.students[i] > search_rollno:
                fib_m = fib_2
                fib_1 = fib_1 - fib_2
                fib_2 = fib_m - fib_1

        if self.students[i] == search_rollno:
            print(f"The Student found at index {i}.")
        else:
            print("The student hasn't attended the training program")
   
     

                

obj = Student()
while True:
    print("\n<---------------CHOICE------------------>")
    print("1. Enter '1' to add roll number of students.")
    print("2. Enter '2' to perform linear search.")
    print("3. Enter '3' to perform sentinel search.")
    print("4. Enter '4' to perform binary search.")
    print("5. Enter '5' to perform fibonacci search.") 
    print("0. Enter any other key to escape.")
    choice = int(input("Enter your choice\n"))
    
    if(choice == 1):
        obj.arr_roll_no()

    elif(choice == 2):
        obj.linear_search()

    elif(choice == 3):
        obj.sentinel_search()

    elif(choice == 4):
        obj.Binary_search()

    elif(choice == 5):
        obj.fibonacchi_search()

    else:
        break


