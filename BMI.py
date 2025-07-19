def calculate_bmi():

    print("Welcome to the BMI Calculator!") 

    weight = float(input("Enter your weight in kilograms : "))

    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    print(f"\nYour calculated BMI is: {bmi:.2f}")
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    print(f"Based on your BMI, you are classified as: {category}")

if __name__ == "__main__":
    calculate_bmi()
