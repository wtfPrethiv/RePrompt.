from pydantic import BaseModel, field_validator

class Prompt(BaseModel):
    
    prompt : str
    llm : str

    @field_validator('prompt')
    def prompt_val(cls, value):
        
        value = value.strip()
        
        if len(value) <  1:
            raise ValueError("Prompt must be atleast a charecter long !!! (even though that shi doesnt make sense but yea)")
        
        return value
