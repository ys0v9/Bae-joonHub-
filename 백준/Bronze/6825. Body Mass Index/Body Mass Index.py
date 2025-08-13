def get_bmi(weight, height):
    return weight / (height * height)


def body(weight, height):
    result = ""
    
    bmi = get_bmi(weight=weight, height=height)
    
    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 25:
        result = "Normal weight"
    elif bmi >= 25:
        result = "Overweight"
        
    return result


if __name__ == "__main__":
    weight = float(input())
    height = float(input())
    
    print(body(weight = weight, height = height))