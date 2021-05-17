from pydantic import BaseModel
from datetime import datetime


class StudentSchema(BaseModel):
    id : str
    registration_number = str
    first_name = str
    last_name : str
    gender:str
    date_of_admission = datetime
    created_date = datetime
    last_modified_date = datetime
