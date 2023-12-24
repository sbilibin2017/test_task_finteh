from pydantic import Field, BaseModel
import os

PREFIX = "POSTGRES"

class DBSettings(BaseModel):
    name: str = Field(default=os.environ.get(f"{PREFIX}_NAME"))
    user: str = Field(default=os.environ.get(f"{PREFIX}_USER"))
    password: str = Field(default=os.environ.get(f"{PREFIX}_PASSWORD"))
    host: str = Field(default=os.environ.get(f"{PREFIX}_HOST"))
    port: int = Field(default=os.environ.get(f"{PREFIX}_PORT"))
    schema_name: str = Field(default=os.environ.get(f"{PREFIX}_SCHEMA"))
