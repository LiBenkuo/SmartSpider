# -*- coding: utf-8 -*-

# `datetime` module supplies classes for manipulating dates and times

# dates are easily constructed and formatted
from datetime import date

now = date.today()
print(now)

print(now.strftime("%y-%m-%d. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1990, 11, 8)
age = now - birthday
print(age.days)
