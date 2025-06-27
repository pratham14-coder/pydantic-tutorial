from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# ✅ Define a Pydantic model for Patient data
class Patients(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the Patient",
            description="Give the name of the patient (max 50 characters)",
            example="Ramesh"
        ),
    ]
    email: EmailStr
    age: Annotated[
        int,
        Field(
            gt=0,
            lt=120,
            title="Age of the patient",
            description="Enter age between 1 and 119"
        ),
    ]
    weight: Annotated[
        float,
        Field(
            gt=0,
            strict=True,
            title="Weight of the patient",
            description="Enter weight greater than 0",
            example=65.5
        ),
    ]
    marriage: Annotated[
        Optional[bool],
        Field(
            default=False,
            title="Marriage status of the patient",
            description="Enter marriage status: True or False"
        )
    ]
    Linkedin_URL: AnyUrl
    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            max_items=5,
            title="Allergies of the patient",
            description="List up to 5 allergies"
        )
    ]
    contact_details: Dict[str, str]  # Must include 'email' and 'phone'

# ✅ Sample patient dictionary
patient_object = {
    "name": "Pratham",
    "email": "prathamsuthar140104@gmail.com",
    "age": 21,
    "weight": 65.5,
    "Linkedin_URL": "https://www.linkedin.com/in/prathamsuthar",
    "contact_details": {
        "email": "prathamsuthar140104@gmail.com",
        "phone": "1234567890"
    },
    "allergies": ["dust", "pollen"]
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
    print("Linkedin_URL:", patient.Linkedin_URL)
    print("Contact Details:", patient.contact_details)
    print("✅ Data inserted successfully.\n")

# ✅ Function to simulate updating patient data
def update_patient_data(patient: Patients):
    print("✏️ Updating Patient Data...")
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("✅ Data updated successfully.\n")

# ✅ Creating a Pydantic model instance
patient1 = Patients(**patient_object)

# ✅ Insert and update operations
insert_patient_data(patient1)
update_patient_data(patient1)
