keep_going = 'y'

while keep_going == 'y':
  sales = float(input('Enter Sales: '))
  comm_rate = float(input('Enter Commission Rate: '))
  commission = sales * comm_rate
  print('Commission Rate: $',round(commission,2))
  keep_going = input('Enter (y) to keep going, otherwise enter (n): ')
print('Thank you for using our service!')

name = input('Enter the name of the employee ')
sales = float(input('Enter your sales amount '))

if sales >= 1 and sales <= 100:
  print('There is no commission')
elif sales >= 101 and sales <= 250:
  salary = round(sales + (sales * 0.10),2)
  print('Name            Salary')
  print('----------------------')
  print(name,'          ',salary)
elif sales >= 251 and sales <= 500:
  salary = round(sales + (sales * 0.15),2)
  print('Name            Salary')
  print('----------------------')
  print(name,'          ',salary)
elif sales >= 501 and sales <= 1000:
  salary = round(sales + (sales * 0.20),2)
  print('Name            Salary')
  print('----------------------')
  print(name,'          ',salary)
elif sales > 1000:
  print(name,'Your surprise is at the management office; Go meet your manager')
else:
  print('Enter a valid number.')

