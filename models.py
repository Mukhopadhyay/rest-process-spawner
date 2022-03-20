from typing import List
from pydantic import BaseModel


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

class MessageResponse(BaseModel):
    msg: str
    timestamp: str

class MultiMessageResponse(BaseModel):
    msgs: List[str]
    timestamp: str