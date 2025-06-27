# ✅ Importing BaseModel from Pydantic
from pydantic import BaseModel


# ✅ Define Address model (nested inside Patient)
class Address(BaseModel):
    Country: str
    State: str
    City: str
    District: str
    Pin_Code: int


# ✅ Define Patient model with nested Address field
class Patient(BaseModel):
    name: str
    age: int
    Gender: bool
    address: Address


# ✅ Function to simulate inserting patient data (like a DB insert)
def insert_patient_data(patient: Patient):
    print("📥 Inserting Patient Data:")
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Patient Gender:", patient.Gender)
    print("Patient City:", patient.address.City)  # Accessing nested model field
    print("✅ Inserted Successfully.\n")


# ✅ Sample address dictionary
Address_object = {
    "Country": "India",
    "State": "Gujarat",
    "City": "Ahmedabad",
    "District": "Motera",
    "Pin_Code": 380005,
}

# ✅ Create Address model instance using dictionary
address1 = Address(**Address_object)

# ✅ Patient dictionary that nests the Address model
patient_dict = {
    "name": "Pratham Suthar",
    "age": 21,
    "Gender": True,
    "address": address1,
}

# ✅ Create Patient model instance
patient1 = Patient(**patient_dict)

# ✅ Convert patient object to dictionary, excluding Pin_Code from address
temp1 = patient1.model_dump(exclude={"address": {"Pin_Code"}})

# ✅ Print the final dictionary and its type
print("🧾 Patient Dictionary (Excluding Pin_Code):")
print(temp1)
print("Type:", type(temp1), "\n")

# ✅ Insert operation
insert_patient_data(patient1)
