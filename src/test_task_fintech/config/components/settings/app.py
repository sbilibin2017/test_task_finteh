from pydantic import Field, BaseModel
import os

PREFIX = "APP"

class AppSettings(BaseModel):
    host: str = Field(default=os.environ.get(f"{PREFIX}_HOST"))
    port: str = Field(default=os.environ.get(f"{PREFIX}_PORT"))
    allowed_hosts: str = Field(default=os.environ.get(f"{PREFIX}_ALLOWED_HOSTS"))
    secret_key: str = Field(default=os.environ.get(f"{PREFIX}_SECRET_KEY"))
    debug: int = Field(default=os.environ.get(f"{PREFIX}_DEBUG"))
    static_url: str = Field(default=os.environ.get(f"{PREFIX}_STATIC_URL"))
