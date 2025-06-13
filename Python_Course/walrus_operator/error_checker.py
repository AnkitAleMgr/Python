word = "error"
not_fount_list = list()

# with open("text.txt", "r") as f:
#     for line in f:
#         print(line.strip())  # prints each line without newline chars

with open("text.txt","r") as file:
    lines = file.read().splitlines()
    for index, line in enumerate(lines):
        print(f"Line {index}: {line}")
