
#Conversion factor for F to C
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

#conversion factor for C to F

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    '''A function take F and convert it C'''
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    '''Take celsius value and convert it in to Fahrenheit'''
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR*celsius + 32
    return fahrenheit

while True:
    #Prompt users to enter temprature to be converted 
    temp = int(input("Enter the temperature to convert: "))
    
    #Choose the unit of the temp you entered 

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if not temp.is_integer():
        
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    if unit == "C":
        current_temprature = convert_to_fahrenheit(temp)
        print(f'{temp}°C is {current_temprature}°F')
        break
    elif unit == "F":
        current_temprature2 = convert_to_celsius(temp)
        print(f"{temp}°F is {current_temprature2}°C")
        break       

