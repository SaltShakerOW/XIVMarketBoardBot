import requests, json 
import pandas as pd

def get_item_data(itemID: str, threshold_price: int = 999999999, num_of_results: int = 10):
    
    output_array = []
    request = requests.get(f'https://universalis.app/api/v2/North-America/{itemID}?listings={num_of_results}')
    
    #HTTP Error Handling
    if request.status_code != 200:
        print(f"Request not successful: HTTP Error {request.status_code}")
        return {"results": []}
    
    #Parsing RAW Universalis Data
    request = json.loads(request.text)
    for listing in request["listings"]:
        if listing["pricePerUnit"] <= threshold_price:
            output_array.append(listing)
    return {"results": output_array}

def does_item_exist(name: str):
    try:
        name_to_id(name)
        return True
    except IndexError:
        print("Item doesn't exist within database")
        return False
    except Exception as e:
        print("Other Error")
        return False
    
def name_to_id(name: str) -> int:
    database_url = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/refs/heads/master/csv/Item.csv" #link to datamined item database
    response = requests.get(database_url) #check if URL is still valid
    if response.status_code == 200: #if yes, extract the itemID of the name parameter
        database = pd.read_csv(database_url, low_memory=False)
        database["9"] = database["9"].str.lower()
        result = database[database["9"].isin([str.lower(name)])]
        try:
            return int(result.iloc[0]["key"])
        except:
            return 0
    else: #if not, produce an error and return nothing
        print("Error: Database not found. Please check database link or network connection.")
        return None
    
def id_to_name(id: int) -> str:
    database_url = "https://raw.githubusercontent.com/xivapi/ffxiv-datamining/refs/heads/master/csv/Item.csv" #link to datamined item database
    response = requests.get(database_url) #check if URL is still valid
    if response.status_code == 200: #if yes, extract the itemID of the name parameter
        database = pd.read_csv(database_url, low_memory=False)
        result = database[database['key'].isin([str(id)])]
        try:
            return result.iloc[0]['9']
        except:
            "N/A"
    else: #if not, produce an error and return nothing
        print("Error: Database not found. Please check database link or network connection.")
        return None

if __name__ == "__main__": #execution code for testing these functions
    #print(name_to_id("Ice Shard"))
    #print(does_item_exist("General-purpose jet Black Dye"))
    print(id_to_name(13115))