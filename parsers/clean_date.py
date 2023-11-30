from typing import List
from models.patents_md import Patent

def clean_date(dataToClean: List[Patent]):
    for item in dataToClean:
        # Check if the 'patent_expiration_date' field exists in the object
        if hasattr(item, "patent_expiration_date"):
            # Extracting the date part from the ISO format
            iso_date = item.patent_expiration_date.split("T")[0]
            # Assigning the date part back to the patent_expiration_date field
            item.patent_expiration_date = iso_date
        else:
            item.patent_expiration_date = "UNKNOWN"

    return dataToClean
