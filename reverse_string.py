###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: Extra Credit
# Program: reverse_string.py
###############################


def main():
	string = input("Please enter the string you wish to be reversed: ")
	reversed_string = ""
	for x in range(len(string)):
		idx = len(string) - x - 1
		reversed_string = reversed_string + string[idx]
	print(reversed_string)
	return reversed_string

if __name__ == '__main__':
	main()

