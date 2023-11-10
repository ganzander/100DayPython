def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  

def days_in_month(yr,d):
  if is_leap(yr)==True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
  else:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
  return month_days[d-1]
  

year = int(input("Enter the year: ")) 
month = int(input("Enter the month: "))
days = days_in_month(year, month)
print(days)

