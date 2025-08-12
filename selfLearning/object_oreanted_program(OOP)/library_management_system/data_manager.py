import pandas as pd
import os, shutil

main_folder_path = os.path.join(os.path.dirname(__file__))
working_dir_path = os.getcwd()

def save_to_csv(data,file_name):
    
    related_path = os.path.relpath(main_folder_path, working_dir_path)
    related_path = os.path.join(related_path,"csv_files/",file_name)
    # print(related_path)
# 
    # print(file_name)
    # path = f"csv_files"
    # print(related_path)

    df = pd.DataFrame(data)
    df.to_csv(related_path)

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

    needed_folder.add("libraries.csv")

    # deleting not needed folder
    all_folder = set(os.listdir(needed_folder_path))
    unneeded_folder = all_folder - needed_folder

    for item in unneeded_folder:
        item_path = os.path.join(needed_folder_path, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            continue
        if os.path.isfile(item_path):
            os.remove(item_path)


    
    # length = os.listdir(needed_folder_path).__len__()
    
    
    


if __name__ == "__main__":
    pass