import sys
weight = input("Please enter your weight in pounds:")
height = input("Please enter your height in inches:")
BMI = float(weight) * 703 / (float(height) * float(height));
print("Your body mass index (BMI) is " + str(BMI))