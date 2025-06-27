# ✅ Importing necessary modules
from pydantic import BaseModel, model_validator
from typing import List, Dict, Optional


# ✅ Define the Pydantic model for validating patient data
class Patients(BaseModel):
    # 🧑‍⚕️ Basic patient fields with type validation
    name: str  # Must be a string
    age: int  # Must be an integer (will be auto-converted if string like "90")
    email: str  # Must be a string (you can use EmailStr for email format check)
    weight: float = 0.0  # Default value 0.0 if not provided
    marriage: bool = False  # Default value False if not provided
    allergies: Optional[List[str]] = None  # Optional list of allergy strings
    contact_details: Dict[
        str, str
    ]  # Dictionary with required fields like 'phone', 'email'

    # ✅ Model-level validator (runs after all fields are validated)
    @model_validator(
        mode="after"
    )  # `mode="after"` means this runs after all fields are parsed
    def validate_emergency_contanct(cls, model):
        # 💡 If patient's age is above 60, check for presence of "emergency" in contact_details
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patient older than 60 must have an emergency contact")
        return model  # return the validated model


# ✅ Simulate incoming patient data from a JSON or API
patient_object = {
    "name": "Pratham",
    "age": "90",  # String input will be cast to int automatically
    "email": "pratham@icic.com",
    "contact_details": {
        "email": "pratham@icic.com",
        "phone": "1234567890",
        "emergency": "1212111200",  # ✅ Required if age > 60
    },
}


# ✅ Simulate inserting patient into the database (e.g., print/save)
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


# ✅ Simulate updating patient record
def update_patient_data(patient: Patients):
    print("✏️ Updating Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("✅ Data updated successfully.\n")


# ✅ Step 1: Create a validated model instance from dictionary using unpacking (**)
# At this point:
# - all field types are validated and converted
# - `@model_validator` logic is also checked
patient1 = Patients(**patient_object)

# ✅ Step 2: Perform operations on the validated model
insert_patient_data(patient1)
update_patient_data(patient1)
