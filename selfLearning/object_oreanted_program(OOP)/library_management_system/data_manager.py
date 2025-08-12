import pandas as pd
import os

def save_to_csv(data,file_name ,folder = None):
    
    # finding current folder path:
    # if folder:
    #     path = os.path.join(os.path.dirname(__file__)+ "/csv_files/"+folder+ ""+ file_name)
    # else:
    path = os.path.join(os.path.dirname(__file__)+ "/csv_files/"+ file_name)
    df = pd.DataFrame(data)
    df.to_csv(path_or_buf = path)

def load_to_csv():
    pass

if __name__ == "__main__":
    pass