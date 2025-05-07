import time


def main():
    second = length_asker()
    timer(second)


def length_asker():
    while True:
        length = input("\nInput time in second \n")
        print("")
        if length.isdigit():
            return int(length)
        else:
            print("Invalid input. Please try again \n")

def timer(second):
    while second:
        min, seconds = divmod(second, 60)
        hour, min = divmod(min, 60)
        Time = f"{hour:02d}:{min:02d}:{seconds:02d}"
        print(f"\rTime left: {Time}", end= "", flush= True)
        time.sleep(1)
        second -= 1
    print(f"\rTime up!!!!!!!!!            ")

if __name__ == "__main__":
    main()