print('  -Calculator-  ')

FirstNumber = int(input('Enter the First Number : '))
SecondNumber = int(input('Enter the Second Number : '))
print('+ , - , * , /  ?')
Action = input(' : ')
if Action == '+':
    print(FirstNumber + SecondNumber)
if Action == '-':
    print(FirstNumber - SecondNumber)
if Action == '*':
    print(FirstNumber * SecondNumber)
if Action == '/':
    print(FirstNumber / SecondNumber)
