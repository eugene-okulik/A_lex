import datetime

current_date = "Jan 15, 2023 - 12:05:33"

pyton_date = datetime.datetime.strptime(current_date, '%b %d, %Y - %H:%M:%S')

print(datetime.datetime.strftime(pyton_date, '%B'))
print(datetime.datetime.strftime(pyton_date, '"%d.%m.%Y, %H:%M"'))
