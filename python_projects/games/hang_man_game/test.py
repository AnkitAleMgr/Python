import os

current_dir = os.path.dirname(__file__)
print(current_dir)


os.chdir("../..")
# new_dir = os.path.dirname(__file__)
new_dir= os.getcwd()
os.listdir()



print(new_dir)