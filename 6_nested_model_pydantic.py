from pydantic import BaseModel


# ✅ Address model for structured location data
class Address(BaseModel):
    country: str
    state: str
    city: str
    district: str
    pin_code: int


# ✅ Patient model with nested Address
class Patient(BaseModel):
    name: str
    age: int
    gender: bool  # True = Male, False = Female
    address: Address


# ✅ Service function to handle patient insertion logic
def insert_patient_data(patient: Patient) -> None:
    print("📥 Inserting Patient Record")
    print(f"Name        : {patient.name}")
    print(f"Age         : {patient.age}")
    print(f"Gender      : {'Male' if patient.gender else 'Female'}")
    print(f"City        : {patient.address.city}")
    print("✅ Patient data inserted successfully.\n")


# ✅ Sample input data (typically from a form or API)
address_data = {
    "country": "India",
    "state": "Gujarat",
    "city": "Ahmedabad",
    "district": "Motera",
    "pin_code": 380005,
}

patient_data = {
    "name": "Pratham Suthar",
    "age": 21,
    "gender": True,
    "address": Address(**address_data),
}

# ✅ Create a Patient object from structured data
patient = Patient(**patient_data)

# ✅ Process the patient record
insert_patient_data(patient)
