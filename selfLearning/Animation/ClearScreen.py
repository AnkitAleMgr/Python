import os

def screenCleaner():
    if os.name == "nt":
        os.system("clr")
    else:
        os.system("Clear")
