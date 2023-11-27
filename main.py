import requests
import pandas as pd
from parsers.clean_date import clean_date
from models.patents_md import Patent

response = requests.get("https://data.nasa.gov/resource/gquh-watm.json")
data = response.json()

new_data = clean_date(data)

# Convert each item in new_data to a Patent object
patent_objects = [Patent(**item) for item in new_data]

# Convert the list of Patent objects to a list of dictionaries using model_dump()
dict_data = [patent.model_dump() for patent in patent_objects]

# Convert the list of dictionaries to a DataFrame
data_df = pd.DataFrame(dict_data)

# Save the DataFrame to a CSV file
csv_path = 'my_data.csv'
data_df.to_csv(csv_path, index=False)

print("File saved")
