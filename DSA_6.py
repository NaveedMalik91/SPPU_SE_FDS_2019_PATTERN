class Student:
    def __init__(self):
        self.stud_scores = [] #students array
        self.n = 0            #number of students

    def create_arr(self):
        self.n = int(input("Enter the total number of students: \n"))
        for i in range(self.n):
            values  = float(input(f"Enter the score of student {i + 1}: "))
            self.stud_scores.append(values)
        return self.stud_scores
    
    #<-----------------Partition Function--------------->
    def partition(self, start, end):
        #setting pivot at starting position
        pivot = self.stud_scores[start]
        count = 0
        #values number of values less than pivot
        for n in range(start + 1, end + 1):
            if self.stud_scores[n] <= pivot:
                count += 1
        #setting correct pivot index
        pivot_index = start + count
        #Swapping pivot previous position with actual position
        temp = self.stud_scores[pivot_index]
        self.stud_scores[pivot_index] = self.stud_scores[start]
        self.stud_scores[start] = temp


        #setting variables for starting index and ending index
        i = start
        j = end

        #Checking the values left to pivot and right to pivot are in actual position?
        while i < pivot_index and j > pivot_index:
            #Comparing rightwards and leftward value to pivot with it
            while self.stud_scores[i] < pivot:
                i += 1
            while self.stud_scores[j] > pivot:
                j -= 1

            if i < pivot_index and j > pivot_index:

                temp = self.stud_scores[j]
                self.stud_scores[j] = self.stud_scores[i]
                self.stud_scores[i] = temp

                #self.stud_scores[i], self.stud_scores[j] = self.stud_scores[j], self.stud_scores[i]

        #Return pivot index i.e actual index of pivot in sorted array
        return pivot_index  
    
    #<--------------Quick Sort Function----------------->
    def quickSort(self, start, end):
        if start < end:
            pivot_index = self.partition(start, end) #Calling partition function and storing index of pivot to variable
            self.quickSort(start, pivot_index - 1)    # calling Quicksort function to sort values left to pivot
            self.quickSort(pivot_index + 1, end)      #Calling Quick sort function to sort values right to pivot
        return self.stud_scores
    
    #<----------------Top five Values--------------------->

    def top_five(self):
        self.quickSort(0,len(self.stud_scores)-1)
        if len(self.stud_scores) < 5:
            print("Scores are less than required")
        else:
            scores = []
            self.quickSort(0, len(self.stud_scores) - 1)
            for i in range(self.n):
                if i > 4:
                    break
                scores.append(self.stud_scores[-1-i])  #Will take values from index 0 to 4/first five values
            print(f"The top five scores are: {scores}")

#<-------------------------Main---------------------------->

obj = Student()

while True:
    print("\n<-------------CHOICE-------------->")
    print("1. Enter '1' to enter scores of students")
    print("2. Enter '2' to Perform Quick Sort")
    print("3. Enter '3' to display top five scores")
    print("4. Enter any other key to Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        result1 = obj.create_arr()
        print("The array of scores of students =", result1)
    elif choice == '2':
        obj.quickSort(0, len(obj.stud_scores) - 1)
        print("The Sorted array of scores of students =", obj.stud_scores)
    elif choice == '3':
        obj.top_five()
    else:
        break