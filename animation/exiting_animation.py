import random, time

def exit_():
    random_number = random.randint(2,3)
    for _ in range(random_number):
        display = "Exiting"
        for _ in range(5):
            time.sleep(0.4)
            print(f"\r{display:<12}",end="",flush=True)
            display += "."
        print("\r",end="", flush=True)
    exit()  

if __name__ == "__main__":
    exit()
