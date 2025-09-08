# This is program-29.py
'''
Write a Python Program to calculate your Body Mass Index.
Body Mass Index (BMI) is a measure of body fat based on an individual's weight and
height. It is commonly used as a screening tool to categorize individuals into different weight
status categories, such as underweight, normal weight, overweight, and obesity.
The BMI is calculated using the following formula:
    BMI = weight (kg) / (height (m))^2
For example, if a person weighs 70 kilograms and is 1.75 meters tall, the BMI would be calculated as:
    BMI = 70 / (1.75)^2 = 22.86
Alternatively, in the imperial system:
    BMI = (weight (lbs) / (height (in))^2) * 703
For example, if a person weighs 154 pounds and is 68 inches tall, the BMI would be calculated as:
    BMI = (154 / (68)^2) * 703 = 23.41
BMI provides a general indication of body fatness but does not directly measure body fat or
distribution. It is widely used in public health and clinical settings as a quick and simple tool
to assess potential health risks associated with weight. Different BMI ranges are associated
with different health categories, but it's important to note that BMI has limitations and does
not account for factors such as muscle mass or distribution of fat.
'''

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your Body Mass Index (BMI) is:", bmi)
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")