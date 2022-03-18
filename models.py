from pydantic import BaseModel
from typing import List


class IndexResponse(BaseModel):
    endpoints: List[str]
    start_time: str
    
class CreateRequestBody(BaseModel):
    value: int

class CreateResponse(BaseModel):
    msg: str

class ProcessesResponse(BaseModel):
    value: str
    pid: int
    timestamp: str

