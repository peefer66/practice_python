import datetime

name = input('What is your name? ')
age = input('What is your age? ')
now = datetime.datetime.now()
year = (now.year - int(age)) + 100

print ('Hello {} you will be 100 years old in {}'.format(name, year))
