# from multiprocessing import process
import time
import random

def advance_loding_animation():
    loop = random.randint(2, 3)
    for i in range(loop):
        display = "Processing"
        for i in range(5):
            time.sleep(0.5)
            print(f"\r{display:<20}", end="", flush=True)
            display += "."
    print("\r", end="", flush=True)

def main():
    advance_loding_animation()

if __name__ == "__main__":
    main()