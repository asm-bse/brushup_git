

def c_to_f(celsius: float) -> float:
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


filepath = 'brushup/celsius.txt'
print('\n')
try:
    with open(filepath, 'r') as file:
        for line in file:
            try:
                cel = float(line.strip())
                far = c_to_f(cel)
                print(f'{cel} degrees Celsius is {far} degrees Fahrenheit\n')
            except ValueError:
                print(f'Invalid temperature value: {line.strip()}\n')
except FileNotFoundError:
    print(f"File {filepath} not found")

print("tets")