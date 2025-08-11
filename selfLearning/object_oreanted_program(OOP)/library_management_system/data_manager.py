import pandas as pd

def save_to_csv(data, file_path):
    
    df = pd.DataFrame(data)
    print(df.to_string())

def load_to_csv():
    pass

if __name__ == "__main__":
    pass