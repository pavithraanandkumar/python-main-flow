int = 10
float = 20.5
string = "The result is: "
list = [1, 2, 3, 4, 5]
def arithmetic(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

results = []
for num in list:
    add, sub, mul, div = arithmetic(int, num)
    results.append((add, sub, mul, div))

for i, result in enumerate(results):
    print(f"{string}{list[i]}")
    print(f"Addition: {result[0]}")
    print(f"Subtraction: {result[1]}")
    print(f"Multiplication: {result[2]}")
    print(f"Division: {result[3]}")
    print("----------")
    
