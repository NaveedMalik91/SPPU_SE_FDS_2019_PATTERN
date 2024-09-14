class String_operations:
    def __init__(self):
        self.strng = ""
        self.str_len = 0
    #<----------------------STRING LENGHT--------------------->
    def length_str(self):
        str_len = 0
        for val in self.strng:   #iterates through each and every element in string including special symbols LIKE SPACE AND SYMBOLS
            str_len +=1
        return str_len
    
    #<---------------------STRING FROM USER---------------------> 
    def input_str(self):
        self.strng = input("Enter any String\n")
    def display_str(self):
        print("\nInput String = ",self.strng)


    #<------------------SPLIT WORDS---------------------------->
    def split_words(self):
        words_list = []             #This will hold all the words in a string
        word_in_str = ""           # This will take charcters of a word during each iteration
        for i in self.strng:
            if i.isalnum() or i == '': # checking Either Space or Digits encounterred
               word_in_str += i           # if condition is true this will append the whole word char by char 

            elif word_in_str:                   # Condition become false
                words_list.append(word_in_str)   #word in string appended to list
                word_in_str = ""                #current word reset to hold next word
                
        if word_in_str:                          # This will check finally all words are appended are not not
           words_list.append(word_in_str) 
        return words_list
    
    #<------------------CHARACTER FREQUENCY---------------------------->

    def character_frequency(self):
        count = 0
        char_to_search = input("Enter character to search\n")
        for char in self.strng:
            if char == char_to_search:
                count = count+1
        print(f"The character {char_to_search} occur {count} times in string")
    
    #<----------------------LONGEST WORD IN STRING------------------------>

    def the_longest_word(self):
        temp_words_list = self.split_words()    # List of words returned by split function
        longest_word = ""

        for word in temp_words_list:            # As longest word initialized empty so in each iteration its length will 
            if len(word) > len(longest_word):   # be small than succeeding one
                longest_word = word             #each time longest word will be assigned to variable longest_word
        print("The longest word in String is :",longest_word)
    

    #<-----------------------------PALINDROME STRING-------------------------------->
    def is_palindrome(self):
        cleaned_string = self.strng.replace(" ","").lower()      # Remove spaces and convert all characters into lowercase
        Length = len(cleaned_string)
        half_length = Length//2   #created to check half length of string

        for i in range(half_length):
            if(cleaned_string[i] != cleaned_string[Length-i-1]): #this will check whether string from start and from end is matched
                return False
        return True
    #<-----------------------------PALINDROME STRING-------------------------------->
    def first_pos_substrng(self):
        self.str_len = self.length_str()
        sub_string = input("Enter substring whose fist appearance index to find :\n")

        for i in range(self.str_len):
            if self.strng[i:i+len(sub_string)] == sub_string:
                return i                      # if present       
        return -1                              #if not present

    #<------------------------------------ WORD FREQUENCY---------------------------------->
    def count_of_word(self):
        count = 0
        words = self.split_words()
        word_freq_search = input("Enter the word whose frequency to find\n")
        for i in words:
            if(i == word_freq_search):
                count +=1
        print(f"The word {word_freq_search} occur {count} times in string")
        return count
       
    
    #<-----------------------------------MAIN----------------------------------------------->

obj = String_operations()
while True:
    print("\n<---------------CHOICE-------------->")
    print("1. Enter '1' to input the string.")
    print("2. Enter '2' to display the string.")
    print("3. Enter '3' to check the frequency of a character.")
    print("4. Enter '4' to check if the string is a palindrome.")
    print("5. Enter '5' to check count of word.")
    print("6. Enter '6' to display the largest word.")
    print("7. Enter '7' to check for first appearance index of a subtring.")
    print("---Enter any other key to Exit.---")
    choice = int(input("\nEnter your Choice\n"))

    if(choice == 1):
        obj.input_str()

    elif(choice == 2):
        obj.display_str()

    elif(choice == 3):
        obj.display_str()
        obj.character_frequency()

    elif(choice == 4):
        obj.display_str()
        result = obj.is_palindrome()
        if result:
            print("The input string is a palindrome.")
        else:
            print("The input string is not a palindrome.")
       
    elif(choice == 5):
        obj.display_str()
        obj.count_of_word()

    elif(choice == 6):
        obj.display_str()
        obj.the_longest_word()

    elif(choice == 7):
        obj.display_str()
        position = obj.first_pos_substrng()
        if position != -1:
            print(f"The first appearance of the substring is at index {position}.")
        else:
            print("The substring is not found in the string.")

    else:
        break