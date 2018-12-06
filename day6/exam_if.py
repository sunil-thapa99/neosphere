#!/usr/bin/env python3
def main():
	marks = int(input("Enter your marks: "))

	if marks < 0 or marks > 100:
		print("Invalid Entry!!!")
	elif marks >= 80:
		print("!!! Distinction !!!")
	elif marks >= 70:
		print("!!! First Division !!!")
	elif marks >= 60:
		print("!!! Second Division !!!")
	elif marks >= 50:
		print("!!! Third Division !!!")
	elif marks >= 40:
		print("!!! Passed !!!")
	else:
		print("!!! You have failed the exam !!!")

if __name__ == "__main__":
	main()