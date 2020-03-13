print("Python Error Handling ")
age = -1
while age <= 0:
    try:
        age = int(input('enter your age in years: '))
        if age <= 0:
            print('your age must be positive')
    except(ValueError, EOFError):
        print('invalid response')




