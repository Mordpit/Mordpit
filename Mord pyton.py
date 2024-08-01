# Situation: Deciding what to wear based on the weather

def suggest_clothing(temperature):
    if temperature >= 25:
        return "It's hot outside! Wear light clothing like shorts and a t-shirt."
    elif temperature >= 15:
        return "It's mild outside. A light jacket and jeans should be comfortable."
    elif temperature >= 5:
        return "It's cool outside. Consider wearing a sweater or a long-sleeve shirt."
    else:
        return "It's cold outside! Bundle up with a heavy jacket, scarf, and gloves."

def main():
    print("Welcome to the Clothing Advisor!")
    while True:
        try:
            temperature = float(input("Enter the temperature in Celsius: "))
            advice = suggest_clothing(temperature)
            print(advice)
            break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()


# Situation: Deciding what to wear based on the weather

def suggest_clothing(temperature):
    if temperature >= 25:
        return "It's hot outside! Wear light clothing like shorts and a t-shirt."
    elif temperature >= 15:
        return "It's mild outside. A light jacket and jeans should be comfortable."
    elif temperature >= 5:
        return "It's cool outside. Consider wearing a sweater or a long-sleeve shirt."
    else:
        return "It's cold outside! Bundle up with a heavy jacket, scarf, and gloves."

def main():
    print("Welcome to the Clothing Advisor!")
    while True:
        try:
            temperature = float(input("Enter the temperature in Celsius: "))
            advice = suggest_clothing(temperature)
            print(advice)
            break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
