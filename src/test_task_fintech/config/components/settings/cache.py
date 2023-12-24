from pydantic import Field, BaseModel
import os

PREFIX = "REDIS"

class CacheSettings(BaseModel):
    password: str = Field(default=os.environ.get(f"{PREFIX}_PASSWORD"))
    db: int = Field(default=os.environ.get(f"{PREFIX}_DB"))
    host: str = Field(default=os.environ.get(f"{PREFIX}_HOST"))
    port: int = Field(default=os.environ.get(f"{PREFIX}_PORT"))    