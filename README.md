# rest-process-spawner
Example scenario of executing lengthy functions using python Rest APIs and processes.

## Description
The server is written in [FastAPI](https://fastapi.tiangolo.com/). But the idea works for FastAPI, flask alike. No async is used in this project. 

**Note:** I was stuck for some case like this some time back, so putting it up on my page, in case anyone finds this helpful :D

## Usage
Consider the scenario, where you need to run some method, which you know will take a long time to run, but you have nothing to do with its response / return. All you want to do is to run the method and be over with it.
This project is a boilerplate of how that can be dealt with using a rest API and a process based approach.
Checkout the file named `router.py` in both of the `/create` endpoint handlers you'll see that we're creating and starting a process and be done with it. It is a very simple implementation, in your case however it may be more complex, but hopefully you get the idea!

The "lengthy" function in our case is as follows:
```python
def take_some_time(n: Optional[int]=10) -> None:
    time.sleep(n)
    return
```
You'll find this in the `utils.py` script. Good luck!


## Installing the dependencies
```bash
python -m pip install -r requirements.txt
```

## Starting the server
```bash
uvicorn app:app
```

As the server is running visit [`localhost:8000/docs`](http://localhost:8000/docs) to check out the endpoints.

|Endpoint|Method|Description|
|:-------|:-----|:----------|
|`/create`|**GET**|Creates a process with a random value|
|`/create`|**POST**|Creates a process with given value in request body|
|`/processes`|**GET**|Get all processes and their details created by this API|
|`/active`|**GET**|Get all active processes|
|`/kill`|**GET**|Kill the most recent process|
|`/kill_all`|**GET**|Kill all active processes|