from base_class import Converter
Temperature = Converter(
    ["Fahrenheit", "Celsius","Kelvin","Rankine","Delisle"], [1.8,1,1,1.8,-1.5],offsets=[32, 0,273.15,491.67,150] # Units
)
Length = Converter(
    units=["Meters", "Kilometers", "Miles", "Yards", "Feet"],
    factors=[1, 0.001, 0.000621371, 1.09361, 3.28084],
    offsets=[0, 0, 0, 0, 0]
)

# Weight Converter (Grams, Kilograms, Pounds, Ounces)
Weight = Converter(
    units=["Grams", "Kilograms", "Pounds", "Ounces"],
    factors=[1, 0.001, 0.00220462, 0.035274],
    offsets=[0, 0, 0, 0])
if __name__ == "__main__":
# Example conversions
    fahrenheit = 10
    celsius = 37
    print(f"{fahrenheit} Fahrenheit is {Temperature.convert(fahrenheit, 'Fahrenheit', 'Celsius')} Celsius.")
    print(f"{celsius} Celsius is {Temperature.convert(celsius, 'Celsius', 'Fahrenheit')} Fahrenheit.")
    print(f"{celsius} Celsius is {Temperature.convert(celsius, 'Celsius', 'Kelvin')} Kelvin.")
    print(f"{celsius} Celsius is {Temperature.convert(celsius, 'Celsius', 'Rankine')} Rankine.")
    print(f"{celsius} Celsius is {Temperature.convert(celsius, 'Celsius', 'Delisle')} Delisle.")
    print(f"75 Delisle é {Temperature.convert(75, 'Delisle', 'Celsius')}°C.")