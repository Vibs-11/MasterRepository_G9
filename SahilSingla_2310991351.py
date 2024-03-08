def calculate(n1, n2, op):
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        if n2 == 0:
            raise ValueError('Cannot divide by zero')
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    elif op == 'sqrt':
        if n1 < 0:
            raise ValueError('Cannot calculate the square root of a negative number')
        result = n1 ** 0.5
    else:
        raise ValueError('Invalid operator')

    if result.is_integer():
        result = int(result)

    return result

continue_calculating = True
while continue_calculating:
    try:
        number1 = float(input('Enter first number: '))
        op = input('Enter operator (+,-,*,/,^,sqrt): ')

        if op in ['^', 'sqrt']:
            number2 = None
            if op == '^':
                number2 = float(input('Enter second number: '))
            result = calculate(number1, number2, op)
            print('=', result)
        else:
            number2 = float(input('Enter second number: '))
            print(number1, op, number2)
            result = calculate(number1, number2, op)
            print('=', result)

        yes_or_no = input('Continue? (y/n): ')
        if yes_or_no == 'n':
            continue_calculating = False

    except ValueError as e:
        print(e)