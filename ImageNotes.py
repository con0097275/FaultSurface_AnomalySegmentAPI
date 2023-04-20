from pydantic import BaseModel


class ImageNote(BaseModel):
    image: str