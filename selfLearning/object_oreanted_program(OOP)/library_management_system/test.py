from data_manager import save_to_csv

data = {
    "Id": 1, 
    "Name": "Ankit",
    "Age" : 19
}


save_to_csv(data=[data,data,data], file_path="test.csv")