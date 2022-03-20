# Custom scripts
import utils
import models
# Built-ins
import multiprocessing
from typing import List
# Third-party
from fastapi import APIRouter, status, HTTPException, Request


start_time = utils.get_dt()
background_process = None
process_history = []


# Instantiating an APIRouter
router = APIRouter()

# Index route
@router.get('/', tags=['info'], response_model=models.IndexResponse)
def get_index():
    return models.IndexResponse(
        endpoints=[r.path for r in router.routes],
        start_time=start_time
    )

@router.get('/create',
            tags=['processes'],
            status_code=status.HTTP_201_CREATED,
            response_model=models.CreateResponse)
def create_with_random_val():
    global background_process

     ###############################################################
    #       This is where the time consuming function goes        #
    ###############################################################

    background_process = multiprocessing.Process(target=utils.take_some_time)
    background_process.start()
    pid = background_process.pid

    process_history.append(
        models.ProcessesResponse(
            value=utils.get_random_value(), 
            pid=pid, 
            timestamp=utils.get_dt()
        )
    )
    
    return {'msg': f'Started on PID: {pid}'}


@router.post('/create', 
             tags=['processes'], 
             status_code=status.HTTP_201_CREATED,
             response_model=models.CreateResponse)
def create(body: models.CreateRequestBody,):
    global background_process
    
    ###############################################################
    #       This is where the time consuming function goes        #
    ###############################################################
    
    background_process = multiprocessing.Process(target=utils.take_some_time)
    background_process.start()
    pid = background_process.pid
    
    process_history.append(
        models.ProcessesResponse(
            value=body.value, 
            pid=pid, 
            timestamp=utils.get_dt()
        )
    )
    
    return {'msg': f'Started on PID: {pid}'}


@router.get('/processes', 
            tags=['processes'], 
            response_model=List[models.ProcessesResponse])
def get_all_processes():
    return process_history


@router.get('/active', tags=['processes'])
def get_all_active_processes():
    arr = utils.get_active_processes()
    return {'active': arr}


@router.get('/kill', tags=['processes'])
def kill_the_most_recent_process():
    if background_process.is_alive():
        background_process.kill()
        s = 'Killed: {}'.format(background_process)
        return models.MessageResponse(msg=s, timestamp=utils.get_dt())
    else:
        s = 'Process: {} is not alive!'
        return models.MessageResponse(msg=s.format(background_process.pid), 
                                     timestamp=utils.get_dt())


@router.get('/kill_all', tags=['processes'])
def kill_all_active_processes():
    processes = utils.get_active_processes(proc=True)
    strings = []
    for process in processes:
        process.kill()
        strings.append(f'Killed: {str(process)}')
    return models.MultiMessageResponse(msgs=strings, timestamp=utils.get_dt())
