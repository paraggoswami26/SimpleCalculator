a = int(input('Enter the First number: '))
b = int(input('Enter the Second number: '))
c = input('Enter the Operator (+, -, *, /): ')  # Operator as a string

if c == '+':
    print('Result:', a + b)
elif c == '-':
    print('Result:', a - b)
elif c == '*':
    print('Result:', a * b)
elif c == '/':
    if b != 0:  # Check to avoid division by zero
        print('Result:', a / b)
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid Operator:', c)
