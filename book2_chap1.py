unit_price = 49.99
quantity = 30

print(f"Subtotal: ${unit_price * quantity:.2f}")
print(f"Subtotal: ${unit_price * quantity:,.2f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
print(f"Sales Tax Rate {sales_tax_rate:.1%}")


subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax

output = f"""
Subtotal:   ${subtotal:,.2f}
Sales Tax:  ${sales_tax:,.2f}
Total:      ${total:,.2f}
"""
print(output)  # ----------------------------------------------


output1 = f"""
Subtotal:       ${subtotal:>9,.2f}
Sales Tax:      ${sales_tax:>10,.2f}
Total:          ${total:>11,.2f}
"""
print(output1)  # ----------------------------------------------


s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

output2 = f"""
Subtotal:       {s_subtotal:>9}
Sales Tax:      {s_sales_tax:>10}
Total:          {s_total:>11}
"""
print(output2)  # ----------------------------------------------

x = 255
print(x)                # 255
print(bin(x))           # 0b11111111
print(oct(x))           # 0o377
print(hex(x))           # 0xff

print(0b0111)           # 7
print(0b0111)           # 7

first_name = "Alan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + ". " + last_name   # Alan C. Simpson
print(full_name)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1), len(s2), len(s3))    # 0 1 5

print('\n')  # string.methodname(params) --------------------------------------------------
s = "  Write a program that returns the girl's age (0-9) as an integer. "

print("s.capitalize(): ", s.capitalize())
print(f"s.count('r'): {s.count('r'): > 14}")
print("s.find('r'):     ", s.find('r', 15))
print("s.index('r'):    ", s.index('r'))
print("s.isalpha():     ", s.isalpha())
print("s.isdecimal():   ", s.isdecimal())
print("s.islower():     ", s.islower())
print("s.isnumeric():   ", s.isnumeric())
print("s.isprintable(): ", s.isprintable())
print("s.istitle():     ", s.istitle())
print("s.isupper():     ", s.isupper())
print("s.lower():       ", s.lower())
print("s.lstrip():      ", s.lstrip())
print("s.replace('r', 'O'): ", s.replace('r', 'O'))
print("s.rfind('r'):    ", s.rfind('r'))
print("s.rindex('r'):   ", s.rindex('r'))
print("s.rstrip():      ", s.rstrip())
print("s.strip():       ", s.strip())
print("s.swapcase():    ", s.swapcase())
print("s.title():       ", s.title())
print("s.upper():       ", s.upper())
print('\n')


# Uncovering Dates and Times ------------------------------------------
# Working with dates

# Import the datetime module, nickname dt
import datetime as dt
# Store today's date in a variable named today.
today = dt.date.today()                     # NNTP (Network News Transfer Protocol)
print(today)                                # datetime.date(2022, 7, 17)

# Store some other date in a variable called last_of_teens
last_of_teens = dt.date(1999, 12, 31)       # datetime.date(1999, 12, 31)
print(last_of_teens)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)
print('\n')

print(f"{last_of_teens: %a}")       # Weekday, abbreviated
print(f"{last_of_teens: %A}")       # Weekday, full
print(f"{last_of_teens: %w}")       # Weekday number 0-6, where 0 is Sunday
print(f"{last_of_teens: %d}")       # Number day of the month 01-31
print(f"{last_of_teens: %b}")       # Month name abbreviated
print(f"{last_of_teens: %B}")       # Month name full
print(f"{last_of_teens: %m}")       # Month number 01-12
print(f"{last_of_teens: %y}")       # Year without century
print(f"{last_of_teens: %Y}")       # Year with century
print(f"{last_of_teens: %H}")       # Hour 00-23
print(f"{last_of_teens: %I}")       # Hour 00-12
print(f"{last_of_teens: %p}")       # AM/PM
print(f"{last_of_teens: %M}")       # Minute 00-59
print(f"{last_of_teens: %S}")       # Second 00-59
print(f"{last_of_teens: %f}")       # Microsecond 000000-999999
print(f"{last_of_teens: %z}")       # UTC offset
print(f"{last_of_teens: %Z}")       # Time zone
print(f"{last_of_teens: %j}")       # Day number of year 001-366
print(f"{last_of_teens: %U}")       # Week number of year, Sunday as the first day of week, 00-53
print(f"{last_of_teens: %W}")       # Week number of year, Monday as the first day of week, 00-53
print(f"{last_of_teens: %c}")       # Local version of date and time
print(f"{last_of_teens: %x}")       # Local version of date
print(f"{last_of_teens: %X}")       # Local version of time
print(f"{last_of_teens: %%}")       # A % character

print('\n', f"{last_of_teens: %A, %B %d, %Y}")
todays_date = f"{today:%m/%d/%Y}"
print(todays_date)


# %a, %b %d %Y                      Sat, Jun 01 2019
# %x                                06/01/19
# %m-%d-%y                          06-01-19
# This %A %B %d                     This Saturday June 01
# %A %B %d is day number %j of %Y   Saturday June 01 is day number 152 of 2019
# -----------------------------------------------------------------------------


print('\n')
# Working with dates
# variable = datetime.time([hour,[minute,[second,[microsecond]]]])
# midnight = dt.time()
# print(midnight)
# print(type(midnight))

# %I:%M %p                          11:59 PM
# %H:%M:%S and %f microseconds      23:59:59 and 999999 microseconds
# %X                                23:59:59
# -----------------------------------------------------------------------------
import datetime as dt
right_now = dt.datetime.now()
print(right_now)                    # 2022-07-17 12:51:10.525354 (with 10.525354 seconds tacked on)

# datetime(year, month, day, hour, [minute, [second, [microsecond]]])

birthdate = dt.date(1984, 4, 10)
delta_age = (today - birthdate)
print(delta_age)                    # 13977 days, 0:00:00
print(type(delta_age))              # <class 'datetime.timedelta'>

days_old = delta_age.days           # You can convert timedelta to a number of days by tacking .days onto timedelta.
print(type(days_old))               # <class 'int'>


print('\n')
"""To get the number of years, divide the number of days by 365. If you
want just the number of years as an integer, use the floor division
operator (//) rather than regular division (/)."""
years_old = days_old // 365
print(years_old)                    # 38

"""
If you want the number of months, too,
you can ballpark (acceptable range) that just by taking the remainder of dividing the days
by 365 to get the number of days left. Then floor divide that value by 30
(because on average each month has about 30 days) to get a good
approximation of the number of months. Use % rather than / for division
to get just the remainder after the division.
"""
months = (days_old % 365) // 30
print(f"You are {years_old} years and {months} months old.")     # You are 38 years and 3 months old.
