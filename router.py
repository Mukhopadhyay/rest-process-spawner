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
    proc = multiprocessing.active_children()
    arr = [p.pid for p in proc]
    return {'active': arr}


@router.get('/kill', tags=['processes'])
def kill_the_most_recent_process():
    background_process.terminate()
    return 'killed:' + str(background_process.pid)

@router.get('/kill_recent', tags=['processes'])
def kill_most_recent_process():
    try:
        recent_process = process_history[-1]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'No process created!')
    else:
        print('Deleting:', recent_process)
        return 'killed:' + str(recent_process.pid)


@router.get('/kill_all', tags=['processes'])
def kill_all_active_processes():
    proc = multiprocessing.active_children()
    for p in proc: p.terminate()
    return {'msg': 'killed all'}


# @router.post('/test')
# def test(request: Request):
#     token = request.headers.get('Authorization')
#     if token == 123:
#         return 'Workign!'
#     else:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Bad auth {token}')

