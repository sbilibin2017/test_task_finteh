from pydantic import Field, BaseModel
import os

PREFIX = "DOCKER"

class DockerSettings(BaseModel):
    db_host: str = Field(default=os.environ.get(f"{PREFIX}_DB_HOST"))
    cache_host: str = Field(default=os.environ.get(f"{PREFIX}_CACHE_HOST"))
    app_host: str = Field(default=os.environ.get(f"{PREFIX}_APP_HOST"))
