### Exercise 2 - Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper case

class String_me():
    def __init__(self):
        self.string1 = ''

    def get_String(self):
        self.string1 = input("\nGimme a string! Make it cheesy~ \n")
        return

    def print_String(self):
        print(self.string1.upper())
        return


travii = String_me()
travii.get_String()
travii.print_String()