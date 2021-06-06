###############################
# Author: Ben Swinford
# Class: CS 362
# Assignment: Extra Credit
# Program: find_sum.py
###############################


def main():
	arr = input("Enter a list of numbers for the array (i.e. 1, 3, 4, 5, 7, 4): ")
	target_sum = input("Enter the target sum: ")
	index = 0
	answer = []
	for x in range(len(arr)):
		if 0 <= x <= 9:
			for y in range(len(arr)):
				if 0 <= x <= 9:
					if y != index:
						sums = arr[x] + arr[y]
						if sums == target_sum:
							answer.append(arr[x])
							answer.append(arr[y])
							print(answer)
							return
		index = index + 1
	print("There is no combination of two numbers in that list that add to the sum")


if __name__ == '__main__':
	main()
