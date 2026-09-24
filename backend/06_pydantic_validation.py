from pydantic import BaseModel, root_validator, validator

class CreateUser(BaseModel):
    email: str
    password: str 
    confirm_password: str 

    @validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value

    @root_validator()
    def validate_password(cls, values):
        if values.get("password") != values.get("confirm_password"):
            raise ValueError("Passwords do not match")
        return values

CreateUser(email="admn@fastapi.com", password="1234", confirm_password="12234")  # This will raise a validation error