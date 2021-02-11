
print('testing')

def squared_power_list(b,**kwargs):
    if 'start' not in [*kwargs] or 'end' not in [*kwargs]:
        raise ValueError('Hey dude, start and end are kw arguments missing')        
    start=kwargs['start'] if 'start' in [*kwargs] else 0
    end=kwargs['end'] if 'end' in [*kwargs] else 0
    if end<start: 
        return [0]
    else:
        return ([b**i for i in range(start,end+1)])

def polygon_area(*lengths,**kwargs):
    if  'sides' not in [*kwargs]:
        raise ValueError('Hey dude, sides kw arguments missing')        
    sides=kwargs['sides'] if 'sides' in [*kwargs] else 0
    if sides<0 or lengths[0]<0:
        raise ValueError('Hey dude, sides/length cannot be negative')        
    return sum(lengths)*sides/2

def temp_converter(*n,**kwargs):
    if 'temp_given_in' not in [*kwargs]:
        raise ValueError('Hey dude, temp_given_in kw arguments missing')        
    temp_given_in=kwargs['temp_given_in'] if 'temp_given_in' in [*kwargs] else 'f'
    return 5/9*(n[0]-32) if temp_given_in=='f' else 9/5*n[0]+32

def speed_converter(*kmph,**kwargs):
    if 'dist' not in [*kwargs] or 'time' not in [*kwargs]:
        raise ValueError('Hey dude, dist and time are kw arguments missing')        
    if kmph[0]<0:
        raise ValueError('Hey dude, kmph cannot be negative')           
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
        for i in args:
            if type(i)!=int and type(i)!=float:
                raise ValueError('Hey dude, arguments got to be int/float')
                break
    else:
        raise ValueError('Hey dude, No arguments given for processing')
    if kwargs:
        try:
            return fn(*args * repetitons, **kwargs)
        except AttributeError:
            raise ValueError('Hey dude, invalid function name')

    else:
        raise ValueError('Hey dude, No kw arguments given for processing')
    
    
if __name__ == '__main__':
    time_it(squared_power_list, 3,start=0,end=5)
    time_it(polygon_area, 15, sides = 3, repetitons=10)
    time_it(temp_converter, 37.78, temp_given_in = 'c', repetitons=100)
    time_it(speed_converter, 100, dist='km', time='m', repetitons=200)
    