from pydantic import BaseModel


class CreateRequestBody(BaseModel):
    value: int

class CreateResponse(BaseModel):
    msg: str

class ProcessesResponse(BaseModel):
    value: str
    pid: int
    timestamp: str

