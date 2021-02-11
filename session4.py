def squared_power_list(b,**kwargs):
    start=kwargs['start'] if 'start' in [*kwargs] else 0
    end=kwargs['end'] if 'end' in [*kwargs] else 0
    if end<start: 
        return [0]
    else:
        return ([b**i for i in range(start,end+1)])

def polygon_area(*lengths,**kwargs):
    sides=kwargs['sides'] if 'sides' in [*kwargs] else 0
    return sum(lengths)*sides/2

def temp_converter(*n,**kwargs):
    temp_given_in=kwargs['temp_given_in'] if 'temp_given_in' in [*kwargs] else 'f'
    return 5/9*(n[0]-32) if temp_given_in=='f' else 9/5*n[0]+32

def speed_converter(*kmph,,**kwargs):
    dist=kwargs['dist'] if 'dist' in [*kwargs] else 'km'
    time=kwargs['time'] if 'time' in [*kwargs] else 'h'

    if dist=='km':
        d=kmph[0]
    elif dist=='m':
        d=kmph[0]/1000.0
    elif dist=='ft':
        d=kmph[0]/3280.0
    elif dist=='yard':
        d=kmph[0]/1093.61
    
    if time=='d':
        t=d*60
    elif time=='h':
        t=d
    elif time=='m':
        t=d/60
    elif time=='s':
        t=d/60/60
    elif time=='ms':
        t=d/60/60/60
    return t

def time_it(fn, *args, repetitons= 1, **kwargs):
    if args:
        return fn(*args * repetitons, **kwargs)
    else:
        return 0