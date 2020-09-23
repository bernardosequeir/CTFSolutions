

def calc_sundays():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    sundays = 0
    for year in range(1901, 2000+1):
        for month in range(0, 12):
            if(day == 0):
                sundays += 1
                print(year, month)
            if(month == 1 and (year % 4 == 0 and (year % 100 == 0 and year % 400 == 0))):
                day = (day + month_days[1]+1) % 7
            else:
                day = (day + month_days[month]) % 7

    print(sundays)


if __name__ == "__main__":
    calc_sundays()
