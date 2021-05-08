import datetime as dt
import smtplib
import random

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
# print(now)
# print(year)
# print(day_of_week)
# date_of_birth = dt.datetime(year=2001, month=9, day=5, hour=3)
# print(date_of_birth)

my_email = "volumedownjoker@gmail.com"
password = "#Prince100"

if day_of_week == 3:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        # print(random.choice(quotes_list))
        quote = random.choice(quotes_list)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Good Morning\n\n{quote.encode('UTF-8')}"
                            )
