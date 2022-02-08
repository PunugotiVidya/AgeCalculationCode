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
        if stMonth == endMonth:
            remainingDays = endDay-stDay
        else:
            for mnth in range(stMonth+1, endMonth):
                remainingMonths += 1
            if endDay >= stDay:
                remainingMonths += 1
                remainingDays = endDay-stDay
            else:
                calRemainingDays = ((30-stDay)+endDay)
                remainingMonths += calRemainingDays//30
                remainingDays = calRemainingDays-(calRemainingDays//30)*30

    else:
        # if not same remaining month calculation
        for mnth in range(stMonth+1, 13):
            remainingMonths += 1
        for mnth in range(1, endMonth):
            remainingMonths += 1

        if endDay >= stDay:
            remainingMonths += 1
            remainingDays = endDay-stDay
        else:
            calRemainingDays = ((30-stDay)+endDay)
            remainingMonths += calRemainingDays//30
            remainingDays = calRemainingDays-(calRemainingDays//30)*30

    totalYears += remainingMonths//12
    remainingMonths = remainingMonths % 12

    print("Total Years: ", totalYears)

    print("Total remaining Months: ", remainingMonths)

    print("Total Remaining Days: ", remainingDays)


if __name__ == '__main__':
    start_date = input("Enter the Birth Date: ")
    end_date = input("Enter the Current Date: ")
    interest(start_date, end_date)
