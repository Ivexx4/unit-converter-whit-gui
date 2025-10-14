from base_class import Converter
Temperature = Converter(
    ["Fahrenheit", "Celsius","Kelvin","Rankine","Delisle","Reaumur","Newton","Rømer"], [1.8,1,1,1.8,-1.5,0.8,0.33,21/40],offsets=[32, 0,273.15,491.67,150,0,0,7.5] # Units
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
    print(f"75 Delisle é {Temperature.convert(75, 'Delisle', 'Celsius'):.2f}°C.")  # Esperado: 50.0°C
    print(f"32 Fahrenheit é {Temperature.convert(32, 'Fahrenheit', 'Celsius'):.2f}°C.")  # Esperado: 0.0°C
    print(f"300 Kelvin é {Temperature.convert(300, 'Kelvin', 'Fahrenheit'):.2f}°F.")  # Esperado: 80.33°F
    print(f"25 Celsius é {Temperature.convert(25, 'Celsius', 'Rankine'):.2f}°R.")  # Esperado: 536.67°R
    print(f"10 Reaumur é {Temperature.convert(10, 'Reaumur', 'Kelvin'):.2f} K.")  # Esperado: 285.65 K
    print(f"10 Delisle é {Temperature.convert(10, 'Delisle', 'Newton'):.2f}°N.")  # Esperado: 22.00°N
    print(f"10 Rømer é {Temperature.convert(10, 'Rømer', 'Celsius'):.2f}°C.")