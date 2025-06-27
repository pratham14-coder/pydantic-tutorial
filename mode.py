from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: float  # Expected as a float

    # 🔹 Runs before type conversion
    @field_validator("price", mode="before")
    @classmethod
    def clean_price(cls, value):
        print("🔄 Before Parsing:", value, type(value))
        if isinstance(value, str):
            value = value.replace("$", "")  # Remove dollar sign
        return value

    # 🔹 Runs after type conversion
    @field_validator("price", mode="after")
    @classmethod
    def check_price(cls, value):
        print("✅ After Parsing:", value, type(value))
        if value <= 0:
            raise ValueError("❌ Price must be greater than 0")
        return value


# 🔸 Input as integer
item1 = Product(price=250)
print("Final Price (item1):", item1.price)

# 🔸 Input as string with dollar symbol
item2 = Product(price="$199.99")
print("Final Price (item2):", item2.price)
