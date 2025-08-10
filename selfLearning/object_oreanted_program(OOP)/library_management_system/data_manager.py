import pandas as pd

def save_to_csv(data, file_path):
# def save_to_csv():
#     data = [
#     {
#         "Title": "Thor",
#         "Author": "Samgam",
#         "Isbn": "1234-5678-90",
#         "Available": True
#     },
#     {
#         "Title": "Spider Man",
#         "Author": "Anup",
#         "Isbn": "1234-5678-900",
#         "Available": False
#     },
#     {
#         "Title": "Wonder Women",
#         "Author": "Samir",
#         "Isbn": "1234-5678-89",
#         "Available": True
#     }
# ]

    df = pd.DataFrame(data)
    print(df.to_string())
    

def load_to_csv():
    pass

save_to_csv()