import subprocess
import sys

import pytest
import inspect
from test_utils import *
import os.path
import time
import random


# try:
#     import memory_profiler
# except ImportError:
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'memory-profiler'])
# finally:
#     import memory_profiler

# from memory_profiler import memory_usage

import session5 as session



def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_fourspace_equal():
    assert fourspace(session) == False, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_proper_description():
    README_CONTENT_CHECK_FOR=[]
    functions = inspect.getmembers(session, inspect.isfunction)
    for function in functions:
        README_CONTENT_CHECK_FOR.extend([function[0]])
        
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, f"You have not described {c} function well in your README.md file"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



    
def test_create_deck_using_lambda_zip_map():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    assert(session.create_deck_using_lambda_zip_map(vals,suits)==output), 'Not Expected output.  Please validate logic'        

def test_create_deck_using_list_comprehension():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    assert(session.create_deck_using_list_comprehension(vals,suits)==output), 'Not Expected output.  Please validate logic'            


def test_create_deck_using_lambda_zip_map_performance():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    start1 = time.perf_counter()
    session.create_deck_using_lambda_zip_map(vals,suits)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.01, 'It is taking too much time to create_deck_using_lambda_zip_map'

def test_create_deck_using_list_comprehension_performance():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    start1 = time.perf_counter()
    session.create_deck_using_list_comprehension(vals,suits)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.01, 'It is taking too much time to create_deck_using_list_comprehension'

def test_deal_performance():
    start1 = time.perf_counter()
    session.deal(1,2,5)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.01, 'It is taking too much time to create_deck_using_list_comprehension'

def test_deal_for_more_than_2_sets_performance():
    start1 = time.perf_counter()
    session.deal(3,2,5)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.01, 'It is taking too much time to create_deck_using_list_comprehension'

    
def test_create_deck_using_list_comprehension_exception():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    with pytest.raises(ValueError):
        assert session.create_deck_using_list_comprehension(vals,[])
        assert session.create_deck_using_list_comprehension([],suits)
        assert session.create_deck_using_list_comprehension([],[])
        

def test_create_deck_using_lambda_zip_map_exception():
    output=['spades-2', 'spades-3', 'spades-4', 'spades-5', 'spades-6', 'spades-7', 'spades-8', 'spades-9', 'spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace', 'clubs-2', 'clubs-3', 'clubs-4', 'clubs-5', 'clubs-6', 'clubs-7', 'clubs-8', 'clubs-9', 'clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace', 'hearts-2', 'hearts-3', 'hearts-4', 'hearts-5', 'hearts-6', 'hearts-7', 'hearts-8', 'hearts-9', 'hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace', 'diamonds-2', 'diamonds-3', 'diamonds-4', 'diamonds-5', 'diamonds-6', 'diamonds-7', 'diamonds-8', 'diamonds-9', 'diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    with pytest.raises(ValueError):
        assert session.create_deck_using_lambda_zip_map(vals,[])
        assert session.create_deck_using_lambda_zip_map([],suits)
        assert session.create_deck_using_lambda_zip_map([],[])


def test_deal_exception():
    with pytest.raises(ValueError):
        assert session.deal(2,0,5)
        assert session.deal(2,2,1)
        assert session.deal(-1,2,5)
        
def test_decider_exception():
    with pytest.raises(ValueError):
        assert session.decider(['hearts-7', 'hearts-10', 'hearts-8', 'hearts-9', 'hearts-6'],[])
        assert session.decider([],['hearts-7', 'hearts-10', 'hearts-8', 'hearts-9', 'hearts-6'])
        assert session.decider([],[])

def test_get_rank_exception():
    with pytest.raises(ValueError):
        assert session.get_rank([])



def test_performance_decider():
    start1 = time.perf_counter()
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    n=5
    combination={1:'Royal Flush', 2:'Straight Flush', 3:'Four of a Kind', 4:'Full House', 5:'Flush', 6:'Straight', 7:'Three of a Kind', 8:'Two Pair', 9:'One Pair', 10:'High Card'}
    
    for times in range(200):
        combinations=[
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, vals[-n:]))], #1
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, vals[random.choice(range(len(vals)-(n+1))):][:n]))], #2
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,n-1)] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,2))] for item in sublist], #3
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n+1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] for i,j in enumerate(random.sample(vals,2))] for item in sublist], #4
                        # [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, random.sample(vals,n)))], #5
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, random.sample([vals[k] for k in range(len(vals)) if int(k)%2==1],n)))], #5
                        [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),vals[random.choice(range(len(vals)-(n+1))):][:n]))], #6
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n+1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,3))] for item in sublist], #7
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==0 else ([m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==1 else [m+'-'+j for m in random.sample(suits,1)]) for i,j in enumerate(random.sample(vals,3))] for item in sublist], #8
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,min(n,4)))] for item in sublist], #9
                        # [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),random.sample(vals,k=n)))] #10
                        [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),random.sample([vals[k] for k in range(len(vals)) if int(k)%2==0],k=n)))] #10
                    ]

        hands={'Player 1' if i==0 else 'Player 2': [combinations[j],j+1] for i,j in enumerate(random.sample([item for sublist in [[j]*int(50/(i+1)) for i,j in enumerate(range(len(combinations)))] for item in sublist],2))}
        if hands['Player 1'][1]==hands['Player 2'][1]:
            result='no clear winner'
        elif hands['Player 1'][1]>hands['Player 2'][1]:
            result='Player2 is winner'
        else:
            result='Player1 is winner'
        hands['Player 1'][1]=combination[hands['Player 1'][1]]
        hands['Player 2'][1]=combination[hands['Player 2'][1]]
        # print((hands, result))
        session.decider(hands['Player 1'][0],hands['Player 2'][0])
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1, 'It is taking too much time to decide winner'

def test_decider():
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    n=5
    combination={1:'Royal Flush', 2:'Straight Flush', 3:'Four of a Kind', 4:'Full House', 5:'Flush', 6:'Straight', 7:'Three of a Kind', 8:'Two Pair', 9:'One Pair', 10:'High Card'}
    
    for times in range(200):
        combinations=[
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, vals[-n:]))], #1
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, vals[random.choice(range(len(vals)-(n+1))):][:n]))], #2
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,n-1)] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,2))] for item in sublist], #3
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n+1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] for i,j in enumerate(random.sample(vals,2))] for item in sublist], #4
                        # [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, random.sample(vals,n)))], #5
                        [i+'-'+j for i,j in list(zip([random.choice(suits)] * n, random.sample([vals[k] for k in range(len(vals)) if int(k)%2==1],n)))], #5
                        [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),vals[random.choice(range(len(vals)-(n+1))):][:n]))], #6
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n+1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,3))] for item in sublist], #7
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==0 else ([m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==1 else [m+'-'+j for m in random.sample(suits,1)]) for i,j in enumerate(random.sample(vals,3))] for item in sublist], #8
                        [item for sublist in [[m+'-'+j for m in random.sample(suits,int(n/2 if n%2==0 else (n-1)/2))] if i==0 else [m+'-'+j for m in random.sample(suits,1)] for i,j in enumerate(random.sample(vals,min(n,4)))] for item in sublist], #9
                        # [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),random.sample(vals,k=n)))] #10
                        [i+'-'+j for i,j in list(zip(random.sample(suits,n) if n<=len(suits) else suits+random.choices(suits,k=n-len(suits)),random.sample([vals[k] for k in range(len(vals)) if int(k)%2==0],k=n)))] #10
                    ]

        hands={'Player 1' if i==0 else 'Player 2': [combinations[j],j+1] for i,j in enumerate(random.sample([item for sublist in [[j]*int(50/(i+1)) for i,j in enumerate(range(len(combinations)))] for item in sublist],2))}
        if hands['Player 1'][1]==hands['Player 2'][1]:
            result='no clear winner'
        elif hands['Player 1'][1]>hands['Player 2'][1]:
            result='Player2 is winner'
        else:
            result='Player1 is winner'
        hands['Player 1'][1]=combination[hands['Player 1'][1]]
        hands['Player 2'][1]=combination[hands['Player 2'][1]]
        assert session.decider(hands['Player 1'][0],hands['Player 2'][0])==(hands,result), (hands, result)











# def test_invalid_function():
#     with pytest.raises(AttributeError):
#         assert session4.time_it(session4.squared_power_list1, 3,start=0,end=5)
        
# def test_exec_without_args():
#     with pytest.raises(ValueError):
#         assert session4.time_it(print,  sep='-', end= ' ***\n', repetitons=5)
#         assert session4.time_it(session4.squared_power_list, start=0,end=5)
#         assert session4.time_it(session4.polygon_area, sides = 3, repetitons=10)
#         assert session4.time_it(session4.temp_converter, temp_given_in = 'c', repetitons=100)
#         assert session4.time_it(session4.speed_converter,  dist='km', time='m', repetitons=200)

# def test_exec_without_kwargs():
#     with pytest.raises(ValueError):
#         assert session4.time_it(print, 1, 2, 3,  repetitons=5)
#         assert session4.time_it(session4.squared_power_list, 3)
#         assert session4.time_it(session4.polygon_area, 15,  repetitons=10)
#         assert session4.time_it(session4.temp_converter, 37.78,  repetitons=100)
#         assert session4.time_it(session4.speed_converter, 100,  repetitons=200)

# def test_exec_with_str_args():
#     with pytest.raises(ValueError):
#         assert session4.time_it(print, 'a', sep='-', end= ' ***\n', repetitons=5)
#         assert session4.time_it(session4.squared_power_list,'a', start=0,end=5) 
#         assert session4.time_it(session4.polygon_area,'a', sides = 3, repetitons=10) 
#         assert session4.time_it(session4.temp_converter,'a', temp_given_in = 'c', repetitons=100) 
#         assert session4.time_it(session4.speed_converter, 'a', dist='km', time='m', repetitons=200)

# def test_check_kwargs_squared_power_list():
#     with pytest.raises(ValueError):
#         assert session4.time_it(session4.squared_power_list, 3,start1=0,end1=5)

# def test_check_kwargs_polygon_area():
#     with pytest.raises(ValueError):
#         assert session4.time_it(session4.polygon_area, 15, sides2 = 3, repetitons=10)

# def test_check_kwargs_temp_converter():
#     with pytest.raises(ValueError):
#         assert session4.time_it(session4.temp_converter, 37.78, repetitons=100)

# def test_check_kwargs_speed_converter():
#     with pytest.raises(ValueError):
#         assert session4.time_it(session4.speed_converter, 100, dist='km',  repetitons=200)

    
# def test_performance_print():
#     start1 = time.perf_counter()
#     session4.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
#     end1 = time.perf_counter()
#     delta1 = end1 - start1
#     assert delta1 < 0.1

# def test_performance_squared_power_list():
#     start1 = time.perf_counter()
#     session4.time_it(session4.squared_power_list, 3,start=0,end=5)
#     end1 = time.perf_counter()
#     delta1 = end1 - start1
#     assert delta1 < 0.1

# def test_performance_polygon_area():
#     start1 = time.perf_counter()
#     session4.time_it(session4.polygon_area, 15, sides = 3, repetitons=10)
#     end1 = time.perf_counter()
#     delta1 = end1 - start1
#     assert delta1 < 0.1

# def test_performance_temp_converter():
#     start1 = time.perf_counter()
#     session4.time_it(session4.temp_converter, 37.78, temp_given_in = 'c', repetitons=100)
#     end1 = time.perf_counter()
#     delta1 = end1 - start1
#     assert delta1 < 0.1

# def test_performance_speed_converter():
#     start1 = time.perf_counter()
#     session4.time_it(session4.speed_converter, 100, dist='km', time='m', repetitons=200)
#     end1 = time.perf_counter()
#     delta1 = end1 - start1
#     assert delta1 < 0.1

# def test_result_squared_power_list():
#     assert session4.time_it(session4.squared_power_list, 3,start=0,end=5) == [1, 3, 9, 27, 81, 243], 'squared_power_list is not yielding desired result'
# def test_result_squared_power_list_negative():
#     assert session4.time_it(session4.squared_power_list, -3,start=0,end=5) == [1, -3, 9, -27, 81, -243], 'squared_power_list is not yielding desired result'

# def test_result_polygon_area():
#     assert(session4.time_it(session4.polygon_area, 15, sides = 3, repetitons=10)) == 225, 'polygon_area is not yielding desired list'

# def test_result_polygon_area_negative():
#     with pytest.raises(ValueError):
#         assert(session4.time_it(session4.polygon_area, -15, sides = 3, repetitons=10)), 'length / sides cannot be negative'


# def test_result_temp_converter():
#     assert(session4.time_it(session4.temp_converter, 37.78, temp_given_in = 'c', repetitons=100))==100.004, 'temp_converter is not yielding desired list'
# def test_result_speed_converter():
#     assert(round(session4.time_it(session4.speed_converter, 100, dist='km', time='m', repetitons=200),2))==1.67, 'speed_converter is not yielding desired list'

# def test_result_speed_converter_negative():
#     with pytest.raises(ValueError):
#         assert(round(session4.time_it(session4.speed_converter, -100, dist='km', time='m', repetitons=200),2))==1.67, 'distance cannot be negative'
