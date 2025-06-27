# ✅ Importing necessary modules
from pydantic import BaseModel, computed_field
from typing import List, Dict, Optional


# ✅ Define the Pydantic model for validating patient data
class Patients(BaseModel):
    # 🧑‍⚕️ Basic patient fields with type validation
    name: str
    age: int
    email: str
    weight: float = 0.0  # in kilograms
    height: float = 0.0  # in centimeters
    marriage: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[
        str, str
    ]  # Must include keys like 'email', 'phone', 'emergency' (optional)

    # ✅ Computed BMI field (derived from weight and height)
    @computed_field
    @property
    def bmi(self) -> float:
        height_m = self.height / 100  # ✅ Convert height from cm to meters
        if height_m <= 0:
            return 0.0  # avoid division by zero
        bmi = round(self.weight / (height_m**2), 2)  # BMI = kg / m²
        return bmi


# ✅ Simulate incoming patient data (e.g., from API or JSON file)
patient_object = {
    "name": "Pratham",
    "age": "90",  # String will be auto-cast to int
    "email": "pratham@icic.com",
    "weight": 70.5,
    "height": 178.8,
    "contact_details": {
        "email": "pratham@icic.com",
        "phone": "1234567890",
        "emergency": "1212111200",  # Can be optional, based on model_validator
    },
}


# ✅ Function to simulate inserting patient into a database (e.g., just print here)
def insert_patient_data(patient: Patients):
    print("📥 Inserting Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Email:", patient.email)
    print("Weight:", patient.weight)
    print("Height:", patient.height)
    print("BMI:", patient.bmi)
    print("Married:", patient.marriage)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("✅ Data inserted successfully.\n")


# ✅ Function to simulate updating patient record
def update_patient_data(patient: Patients):
    print("✏️ Updating Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("✅ Data updated successfully.\n")


# ✅ Create a validated model instance from the dictionary
patient1 = Patients(**patient_object)

# ✅ Run insert and update operations
insert_patient_data(patient1)
update_patient_data(patient1)
