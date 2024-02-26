user_name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(user_name)

with open('name.txt', 'r') as file:
    name = file.read().strip()
    print(f"Your name is {name}")

with open('numbers.txt', 'r') as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
    total = num1 + num2
    print(f"The sum of the first two numbers is: {total}")

total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(f"The total of all numbers in numbers.txt is: {total}")
