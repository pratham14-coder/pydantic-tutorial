from pydantic import BaseModel, field_validator
from typing import List, Dict, Optional


# ✅ Define a Pydantic model for Patient data with custom field validators
class Patients(BaseModel):
    name: str
    age: int
    email: str
    weight: float = 0.0  # Default value set to 0.0
    marriage: bool = False  # Default value set to False
    allergies: Optional[List[str]] = None  # Optional list of allergies
    contact_details: Dict[str, str]  # Must include 'email' and 'phone'

    # ✅ Email validator - checks domain
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "axis.com", "icic.com"]
        domain = value.split("@")[-1]
        if domain not in valid_domains:
            raise ValueError(
                "❌ Invalid email domain. Allowed: hdfc.com, axis.com, icic.com"
            )
        return value

    # ✅ Name validator - converts to uppercase
    @field_validator("name")
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    # ✅ Age validator before parsing
    @field_validator("age", mode="after")
    @classmethod
    def age_validator(cls, value):
        value = int(value)  # Safe to cast because this code assumes valid input
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be between 1 and 99")


# ✅ Sample patient dictionary (simulate incoming data)
patient_object = {
    "name": "Pratham",
    "age": "50",  # Can be string, will be cast by the validator
    "email": "pratham@icic.com",
    "contact_details": {"email": "pratham@icic.com", "phone": "1234567890"},
}


# ✅ Function to simulate inserting patient data into a database
def insert_patient_data(patient: Patients):
    print("📥 Inserting Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Email:", patient.email)
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
