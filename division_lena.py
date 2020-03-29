print("Please give two numbers that will divide.")
print("Enter 'q', to finish.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_name = input("\nSecond number: ")
    if second_name == 'q':
        break
    try:
        answer = int(first_number)/int(second_name)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        print(answer)