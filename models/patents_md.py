from pydantic import BaseModel

class Patent(BaseModel):
    center: str
    status: str
    case_number: str
    patent_number: str = "UNKNOWN"
    application_sn: str = "UNKNOWN"
    title: str
    patent_expiration_date: str


