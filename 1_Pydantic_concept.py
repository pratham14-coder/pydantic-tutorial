# ✅ Pydantic is a data validation and settings management library for Python
# This script demonstrates how to use Pydantic's BaseModel for type validation and object creation.
# This code only for Type Validation,Data Validataion is in another file 
from pydantic import BaseModel
from typing import List, Dict, Optional

# ✅ Define a Pydantic model for Patient data
class Patients(BaseModel):
    name: str
    age: int
    weight: float = 0.0                     # Default value set to 0.0
    marriage: bool = False                 # Default value set to False
    allergies: Optional[List[str]] = None  # Optional list of allergies
    contact_details: Dict[str, str]        # Must include 'email' and 'phone'

# ✅ Sample patient dictionary (simulate incoming data - could be from API or DB)
patient_object = {
    "name": "Pratham",
    "age": 21,
    "contact_details": {
        "email": "prathamsuthar123@gmail.com",  # Typo fixed in domain name
        "phone": "1234567890"
    }
}

# ✅ Function to simulate inserting patient data into a database
def insert_patient_data(patient: Patients):
    print("📥 Inserting Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.marriage)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("✅ Data inserted successfully.\n")

# ✅ Function to simulate updating patient data
def update_patient_data(patient: Patients):
    print("✏️ Updating Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("✅ Data updated successfully.\n")

# ✅ Creating a Pydantic model instance from the dictionary using unpacking (**)
patient1 = Patients(**patient_object)

# ✅ Insert and update operations
insert_patient_data(patient1)
update_patient_data(patient1)
