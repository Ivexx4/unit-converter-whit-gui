from base_class import Converter
Temperature = Converter(
    {"°F":(1.8,32),"ºC":(1,0),"K":(1,273.15),"ºR":(1.8,491.67),"ºD":(-1.5,150),"ºRe":(0.8,0),"ºN":(0.33,0),"ºRø":(21/40,7.5)}# Units
)

if __name__ == "__main__":
# Example conversions
    print(f"75 ºD = {Temperature.convert(75, "ºD", "ºC"):.2f}°C.")
    print(f"32 ºF = {Temperature.convert(32, "°F", "ºC"):.2f}°C.")
    print(f"300 K = {Temperature.convert(300, 'K', '°F'):.2f}°F.")
    print(f"25 ºC = {Temperature.convert(25, "ºC", "ºR"):.2f}°R.")
    print(f"10 ºRe = {Temperature.convert(10, "ºRe", "K"):.2f} K.")
    print(f"10 ºD = {Temperature.convert(10, "ºD", 'ºN'):.2f}°N.")
    print(f"10 ºRø = {Temperature.convert(10, 'ºRø', "ºC"):.2f}°C.")
