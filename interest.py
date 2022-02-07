import datetime
from dateutil import relativedelta


def interest(start_date, end_date):

    stDay, stMonth, stYear = map(int, start_date.split("-"))
    endDay, endMonth, endYear = map(int, end_date.split("-"))
    totalYears = 0
    remainingMonths = 0
    remainingDays = 0

    for year in range(stYear+1, endYear):
        totalYears += 1

    if stYear == endYear:  # if both starting year and ending year is same ==> month calculation
        for mnth in range(stMonth+1, endMonth):
            remainingMonths += 1
    else:                                  # if not same remaining month calculation
        for mnth in range(stMonth+1, 13):
            remainingMonths += 1
        for mnth in range(1, endMonth):
            remainingMonths += 1

    if stMonth == endMonth:  # if both startMonth and End month is same  remaining days calculation
        remainingDays = endDay-stDay
    else:                    # if both start Month and End month is not same remaining days calculation
        remainingMonths += ((30-stDay+1)+endDay)//30
        remainingDays = ((30-stDay)+endDay) % 30

    print("Total Years: ", totalYears)

    print("Total remaining Months: ", remainingMonths)

    print("Total Remaining Days: ", remainingDays)


if __name__ == '__main__':
    start_date = input("Enter the Birth Date: ")
    end_date = input("Enter the Current Date: ")
    interest(start_date, end_date)
