from ast import main
import pandas as pd
import os

main_folder_path = os.path.join(os.path.dirname(__file__))

def save_to_csv(data,file_name):
    
    # finding current folder path:
    # if folder:
    #     path = os.path.join(os.path.dirname(__file__)+ "/csv_files/"+folder+ ""+ file_name)
    # else:
    # path = os.path.join(main_folder_path, "csv_files", file_name)
    # print(path)
    path = os.getcwd()
    print(path)
    print(main_folder_path)
    # needed_path = main_folder_path.
# 
    # print(file_name)
    # path = f"csv_files"

    df = pd.DataFrame(data)
    # df.to_csv(path_or_buf = path)
    # df.to_csv("here")

def load_to_csv():
    pass


def directory_maker_deleter(no_of_obj : int):
    needed_folder_path = f"{main_folder_path}/csv_files/Library"
    needed_folder = set()
    
    # making needed folder
    for i in range(no_of_obj):
        needed_folder.add(f"library_{i + 1}")
        if not os.path.exists(f"{needed_folder_path}/library_{i+1}"):
            os.mkdir(f"{needed_folder_path}/library_{i+1}")
            print(f"{needed_folder_path}/library_{i+1} has been created")
            print()
    needed_folder.add("libraries.csv")

    # deleting not needed folder
    all_folder = set(os.listdir(needed_folder_path))
    unneeded_folder = all_folder - needed_folder

    for item in unneeded_folder:
        item_path = os.path.join(needed_folder_path, item)
        if os.path.isdir(item_path):
            os.rmdir(item_path)
            continue
        if os.path.isfile(item_path):
            os.remove(item_path)


    
    # length = os.listdir(needed_folder_path).__len__()
    
    
    


if __name__ == "__main__":
    pass