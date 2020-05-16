import sys
import random as rm

score = 500
print("Enter the difficulty level")
print("1. Easy\n2.Moderate\n3.Difficult\n")
difficulty_choice = int(input())

if difficulty_choice == 1:
	end_range = 10
elif difficulty_choice == 2:
	end_range = 50
elif difficulty_choice == 3:
	end_range = 100

number_to_guess = rm.randint(1, difficulty_choice)

input_number = int(input("Enter your guess number:\t"))

while True:
	if input_number == number_to_guess:
		print("Congratulations You have guessed the right number")
		print "Your Score:\t", score
		sys.exit()
	elif input_number < number_to_guess:
		print("The number you have guessed is low")
		input_number = int(input("Enter your new guess number:\t"))
		score = score - 20
	elif input_number > number_to_guess:
		print("The number you have guessed is high")
		input_number = int(input("Enter your new guess number:\t"))
		score = score - 20
