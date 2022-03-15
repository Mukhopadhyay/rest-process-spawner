import multiprocessing
from fastapi import APIRouter, Request, status, HTTPException
from utils import utils

background_process = None
process_mapping = []

router = APIRouter()

@router.get('/', tags=['info'])
def get_index():
    return {'name': 'process-spawner'}

@router.get('/create', tags=['processes'])
def create():
    global background_process
    background_process = multiprocessing.Process(target=utils.take_some_time)
    background_process.start()
    process_mapping.append(background_process.pid)
    return {'msg': 'started on PID: {}'.format(background_process.pid)}

@router.get('/processes', tags=['processes'])
def get_all_processes():
    return process_mapping
