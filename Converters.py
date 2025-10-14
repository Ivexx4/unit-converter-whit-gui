from base_class import Converter
Temperature = Converter(
    ["°F", "ºC","K","ºR","ºD","ºRe","ºN","ºRø"], [1.8,1,1,1.8,-1.5,0.8,0.33,21/40],offsets=[32, 0,273.15,491.67,150,0,0,7.5] # Units
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
    print(f"75 ºD = {Temperature.convert(75, "ºD", "ºC"):.2f}°C.")
    print(f"32 ºF = {Temperature.convert(32, "°F", "ºC"):.2f}°C.")
    print(f"300 K = {Temperature.convert(300, 'K', '°F'):.2f}°F.")
    print(f"25 ºC = {Temperature.convert(25, "ºC", "ºR"):.2f}°R.")
    print(f"10 ºRe = {Temperature.convert(10, "ºRe", "K"):.2f} K.")
    print(f"10 ºD = {Temperature.convert(10, "ºD", 'ºN'):.2f}°N.")
    print(f"10 ºRø = {Temperature.convert(10, 'ºRø', "ºC"):.2f}°C.")
