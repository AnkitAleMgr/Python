import pandas as pd
import os

def save_to_csv(data, file_path):
    
    # finding current folder path:
    path = os.path.join(os.path.dirname(__file__)+ "/csv_files/"+file_path)
    df = pd.DataFrame(data)
    df.to_csv(path_or_buf = path)

def load_to_csv():
    pass

if __name__ == "__main__":
    pass