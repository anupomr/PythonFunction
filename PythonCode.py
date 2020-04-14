name = input("Your name : ")
color = input("Favourite  color : ")
print(name, "Likes", color)
print('*' * 10)

# Type conversion
birth_year = input("Birth Year : ")
print(type(birth_year))
age = 2020 - int(birth_year)  # Conversion
print(type(age))
print(age)

# Mortgage Calculation
house_price = 1000000
is_good_credit = True
down_payment = 0
if is_good_credit:
    down_payment = house_price * .1
else:
    down_payment = house_price * .2
print(f"Down payment: ${down_payment}")

print("Python Error Handling ".upper())
age = -1
while age <= 0:
    try:
        age = int(input('enter your age in years: '))
        if age <= 0:
            print('your age must be positive')
    except(ValueError, EOFError):
        print('invalid response')

print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 2.0, 'C': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print("Unknown grade '{0}' being being ignored")
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))
