from multiprocessing import process
import time
import random

def advance_loding_animation():
    loop = random.randint(2, 5)
    for i in range(loop):
        display = "Processing"
        for i in range(5):
            time.sleep(0.5)
            print(f"\r{display:<20}", end="", flush=True)
            display += "."
    print("\r", end="", flush=True)

advance_loding_animation()