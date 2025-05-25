import time

hour = time.strftime("%H")
hour = int(hour)

try:
    print("\nCurrent time is",hour)
    if hour <= 10:
        print("Good morning")
    elif hour <= 14:
        print("Good afternoon")    
    elif hour <= 18:
        print("Good evening")
    else:
        print("Good nignt")
    print("")
except:
    print("something went wrong....")
