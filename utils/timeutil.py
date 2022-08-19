import datetime

def get_epochtime_ms(input=None):
    if input is None:
        return round(datetime.datetime.utcnow().timestamp() * 1000)
    return round(input * 1000)