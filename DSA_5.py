#<---------------------------Create an array of students------------------>
class student:
    def __init__(self):
        self.stud_percentage = []
        self.num = 0
    
    def create_arr(self):
        self.stud_percentage = []
        self.num = int(input("\nEnter the number of students\n"))
        if self.num < 0:
             print("Invalid input!!!")
        print("Enter percentage of students\n")
        for i in range(self.num):
            percentage = float(input())
            self.stud_percentage.append(percentage)
        print("The array of percentage of students =",self.stud_percentage)
        return self.stud_percentage

#<---------------------------Insertion Sort----------------------------> 
    def insertion_sort(self):

        for i in range(1,len(self.stud_percentage)): # started from 1 as index = 0 element is assumed to be sorted
            #first index value( i = 1)set as current value
            current_element = self.stud_percentage[i]  
            j = i-1
            while j>= 0 and self.stud_percentage[i-1] >current_element :  #(i-1) compare array values with predecessors
                self.stud_percentage[j+1] = self.stud_percentage[j]     #swap possitions
                j = j-1 # traverse sorted array
            self.stud_percentage[j+1] = current_element
        return self.stud_percentage
    
#<-----------------------------------Selection sort----------------------------------->
    def selection_sort(self):
        for i in range(self.num-1):
            for j in range(i+1,self.num):
                if self.stud_percentage[i] > self.stud_percentage[j]:
                    temp = self.stud_percentage[j]
                    self.stud_percentage[j] = self.stud_percentage[i]
                    self.stud_percentage[i] = temp
        return self.stud_percentage
    
#<---------------------------------Bubble Sort---------------------------------------->
    def bubble_sort(self):
        #traverse whole array
        for i in range(self.num):
            #traverse array upto one element less than prevoius(already sorted in each round)
            for j in range(0,self.num-i-1):
                #Compare
                if self.stud_percentage[j] > self.stud_percentage[j+1]:
                    #Swap
                    temp = self.stud_percentage[j+1]
                    self.stud_percentage[j+1] = self.stud_percentage[j]
                    self.stud_percentage[j] = temp
        return self.stud_percentage
        
        


#<--------------------------------Shell Sort-----------------------------------------> 
    def shell_sort(self):
        gap = len(self.stud_percentage)//2

        while gap>0:
            for i in range(gap, len(self.stud_percentage)):
                current_element = self.stud_percentage[i]
                j = i
                while j>= gap and self.stud_percentage[j-gap] > current_element:
                    self.stud_percentage[j] = self.stud_percentage[j-gap]
                    j -= gap
                self.stud_percentage[j] = current_element
            gap = gap//2
        return self.stud_percentage
     

#<---------------------------------Top five scores----------------------------------->
    def top_five(self):
        print("The sorted aray  =",self.shell_sort())
        scores = []
        for i in range(self.num): 
            if i >= 5:
                break
            scores.append(self.stud_percentage[-1-i])   # take first five value from sorted array and append to scores list
        print(f"The top five scores = {scores}")
        



#<-----------------------------------MAIN-------------------------------->  
obj = student()
while True:
    print("\n<--------------CHOICE--------------->")
    print("1. Enter '1' to add names of students.")
    print("2. Enter '2' to perform insertion sort.")
    print("3. Enter '3' to perform shell-sort.")
    print("4. Enter '4' to perform Bubble Sort.")
    print("5. Enter '5' to Display top five scores.")
    print("6. Enter '6' to perform selection sort.")
    print("-->Enter any other key to Exit.")
    choice = int(input("Enter your choice\n"))

    if(choice == 1):
        obj.create_arr()

    elif(choice == 2):
        obj.create_arr()
        result1 = obj.insertion_sort()
        print("The sorted array of scores using insertion sort = ",result1)

    elif(choice == 3):
        obj.create_arr()
        result2 = obj.shell_sort()
        print("The sorted array of scores using shell sort = ",result2)

    elif(choice == 4):
        obj.create_arr()
        result3 = obj.bubble_sort()
        print("The sorted array of scores using  Bubble sort",result3)

    elif(choice == 5):
        obj.top_five()

    elif(choice == 6):
        obj.create_arr()
        result3 = obj.selection_sort()
        print("The sorted array of scores using selection sort = ",result3)

    else:
        break




