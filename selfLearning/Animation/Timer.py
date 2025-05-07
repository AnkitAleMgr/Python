import random
import time

# def main():
#     Processing_animation()

def Processing_animation():
    random_number = random.randint(2,4)
    while random_number <= 5:
        time.sleep(0.7)
        print("Processing.......")
        random_number +=1
    print("")

def short_processing():
    time.sleep(0.5)
    print("processing..")


# if __name__ == "__main__":
#     main()