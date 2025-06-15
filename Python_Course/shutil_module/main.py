import os, shutil
import traceback


def make_files():
    # making files    
    os.system("touch hello1.txt")
    os.system("touch hello2.txt")
    os.system("touch hello3.txt")
    os.system("touch hello4.txt")
    os.system("touch hello5.txt")
    os.system("touch hello6.txt")
    

def make_folders():
    # making 1 folder    
    os.system("mkdir folder1")
    os.system("mkdir folder2")
    os.system("mkdir folder3")
    

def coping_file():
    shutil.copy("hello1.txt", "folder1/copy_hello1.txt")
    shutil.copy2("hello2.txt", "folder1/copy_hello2.txt")

def coping_folder():
    shutil.copytree("folder3", "copy_folder1")

def moving_file():
    shutil.move("hello3.txt", "moved_hello3.txt")

def moving_folder():
    shutil.move("copy_folder1","folder1/moved_folder1")

def removing_folder():
    shutil.rmtree("folder2")

def archiving():
    shutil.make_archive("zip_folder1","zip","folder1")

def coping_archive():
    shutil.copy("zip_folder1.zip","zip_folder2.zip")

def unpacking_archive():
        shutil.unpack_archive("zip_folder1.zip", "unpack_zip_folder")



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# main
def main():
    try:
        make_files()
        make_folders()
        coping_file()
        coping_folder()
        moving_file()
        moving_folder()
        removing_folder()
        archiving()
        coping_archive()
        unpacking_archive()
    except:
        traceback.print_exc()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# entry point
if __name__ == "__main__":
    main()