from datetime import datetime
import datetime as dttt
import time
....much more
current_time = str(datetime.now())  # Returns the current local date and time
time_in_list_system=current_time.split(" ")[0].split("-")
print(time_in_list_system)

int1=4
print(f"hello {int1}")

custom_date = dttt.date(int(date_input[0]), int(date_input[1]), int(date_input[2]))
day_name = custom_date.strftime("%A")   # ChatGPT   # ChatGPT
print(day_name)
title=f"{day_name}, {month_int_name[int(date_input[1])]} {date_input[1]}, {date_input[0]}"
and much more.....
time.sleep(10)