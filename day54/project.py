import time

def time_cal(function):
    def wrapper_function():
        currenttime = time.time()
        function()
        newtime = time.time()
        delayed_time = newtime - currenttime
        print(delayed_time)
    return wrapper_function
    
@time_cal
def time_sleeper():
    time.sleep(2)

time_sleeper()