from calendar import Month
from curses.ascii import isdigit
import datetime
import time


def main():
    date = date_asker()
    print(date)



def date_asker():
        
        try:
           
            date = input("Enter a date (YYYY-MM-DD):   ")
            Date, Month, Day = date.stlipt("-")            # ...existing code...
            def date_asker():
                try:
                    date = input("Enter a date (YYYY-MM-DD):   ")
                    year, month, day = date.split("-")
                    print(f"Year: {year}, Month: {month}, Day: {day}")
                    return date
                except Exception:
                    print("Invalid input")
                    return None
            # ...existing code...

            print(f"Year: {Date},Month: {Month}, Day: {Day}")
        except:
            print("Invalid input")
        
if __name__ == "__main__":
    main()