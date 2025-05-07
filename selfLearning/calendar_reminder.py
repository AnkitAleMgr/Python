from curses.ascii import isdigit
import time


def main():
    date = date_asker()
    print(date)



def date_asker():

    while True:
        date = input("\rEnter a date (YYYY-MM-DD):   ")
        
if __name__ == "__main__":
    main()