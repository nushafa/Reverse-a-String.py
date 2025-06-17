#Input a word or sentence
string = input("Please enter your own string: ")

string2 = ('')
#Reverse the string
for i in string:
    string2 = i + string2
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)    