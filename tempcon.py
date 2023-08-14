# This function converts temperature in Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# This function converts temperature in Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# This function converts temperature in Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

# This function converts temperature in Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin
  
# This function converts temperature in Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# This function converts temperature in Celsius to Kelvin
def celsius_to_kelvin(fahrenheit):
    kelvin = celsius + 273.15
    return kelvin

# Main program
while True:
    # Display available options to the user
    print("\nOptions:")
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")
    print("7. Quit")
    
    # Ask the user for their choice
    choice = input("Select an option (1/2/3/4/5/6/7): ")
    
    # If the user chooses to quit, exit the loop
    if choice == '7':
        print("Goodbye!")
        break
    # If the user chooses a valid temperature conversion option
    elif choice in ['1', '2', '3', '4', '5', '6']:
        # Ask the user for the temperature value to be converted
        temperature = float(input("Enter the temperature: "))
        
        # Perform the chosen temperature conversion
        if choice == '1':
            converted_temp = celsius_to_kelvin(temperature)
            print(f"{temperature}°C is equal to {converted_temp} K")
        elif choice == '2':
            converted_temp = kelvin_to_celsius(temperature)
            print(f"{temperature} K is equal to {converted_temp}°C")
        elif choice == '3':
            converted_temp = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp}°F")
        elif choice == '4':
            converted_temp = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp}°C")
        elif choice == '5':
            converted_temp = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} K is equal to {converted_temp}°F")
        elif choice == '6':
            converted_temp = fahrenheit_to_kelvin(temperature)
            print(f"{temperature}°F is equal to {converted_temp} K")
        
        # Ask the user if they want to round the result to the nearest whole number
        round_option = input("Do you want to round the result to the nearest whole number? (y/n): ").lower()
        
        # If the user wants to round the result, round and display it
        if round_option == 'y':
            rounded_temp = round(converted_temp)
            print(f"Rounded to the nearest whole number: {rounded_temp}")
    else:
        # If the user enters an invalid choice, inform them
        print("Invalid choice. Please select a valid option.")
