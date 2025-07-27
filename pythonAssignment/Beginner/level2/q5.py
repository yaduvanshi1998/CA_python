"""5. You are developing a program that analyzes weather data. 
        Write a Python function that takes a list of temperature readings for a specific location 
        and determines the average temperature, highest temperature, and lowest temperature.
        Input: temperature_readings = [25, 28, 21, 24, 27]
        Output:
        Average Temperature: 25.0
        Highest Temperature: 28
        Lowest Temperature: 21
"""

temperature_readings = [25, 28, 21, 24, 27]

def temp_clac(temperature_readings):
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)
    average_temperature = sum(temperature_readings)/len(temperature_readings)

    return f"highest temperature is: {highest_temperature}, lowest temperature is: {lowest_temperature} and average temperature is: {average_temperature}"

print(temp_clac(temperature_readings))