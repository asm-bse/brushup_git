
def c_to_f(celsius: float) -> float:
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


cel = input("Enter temperature in Celsius: ")

try:
    cel = float(cel)
except ValueError:
    print("Not a number")
else:
    far = c_to_f(cel)
    print(f'{cel} degrees Celsius is {far} degrees Fahrenheit')
