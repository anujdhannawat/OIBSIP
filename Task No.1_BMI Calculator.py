def calculate_bmi(weight, height):
    
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Oasis Infobyte BMI Calculator!\n")
    print("Enter your details - ")

    try:
        weight = float(input("Weight (Kilograms): "))
        height = float(input("Height (Meters): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    if weight <= 0 or height <= 0:
        print("Invalid input. Weight and height must be positive.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\nResults - ")
    print(f"BMI: {bmi:.2f}")
    print(f"Classified Category: {category}")

if __name__ == "__main__":
    main()
