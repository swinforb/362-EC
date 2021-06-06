###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: Extra Credit
# Program: reverse_string.py
###############################


def main():
	string = input("Please enter the string you wish to be reversed: ")
	reversed_string = ""
	string_arr = []
	word = ""
	for x in range(len(string)):
		if string[x] == " ":
			string_arr.insert(0, word)
			word = ""
		else:
			word = word + string[x]
	string_arr.insert(0, word)
	for y in range(len(string_arr)):
		reversed_string = reversed_string + string_arr[y] + " "
	print(reversed_string)
	return reversed_string

if __name__ == '__main__':
	main()

