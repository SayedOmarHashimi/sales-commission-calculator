keep_going = 'y'

while keep_going == 'y':
  name = input('Enter Name: ')
  sales = float(input('Enter Sales: '))
  if sales >= 1 and sales <= 10000:
    print('No Commission')
  elif sales >= 10001 and sales <= 50000:
    salary = round(sales + (sales * 0.10),2)
    print()
    print('NAME                    SALARY')
    print('------------------------------')
    print(name,'                  ',salary)
    print()
  elif sales >= 50001 and sales <= 100000:
    print()
    salary = round(sales + (sales * 0.15),2)
    print('NAME                    SALARY')
    print('------------------------------')
    print(name,'                  ',salary)
    print()
  elif sales >= 100001 and sales <= 250000:
    print()
    salary = round(sales + (sales * 0.20),2)
    print('NAME                    SALARY')
    print('------------------------------')
    print(name,'                  ',salary)
    print()
  else:
    print()
    print('Go see your manager!')
    print()
  keep_going = input('To continue press (y), otherwise please press (n): ')
print()
print('Thank you for using our service, have a good day!')

