import subprocess
import sys

import pytest
import inspect
from test_utils import *
import os.path
import time

try:
    import memory_profiler
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'memory-profiler'])
finally:
    import memory_profiler

from memory_profiler import memory_usage

import session4


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_fourspace_equal():
    assert fourspace(session4) == False, 'Not all spaces before lines are a multiple of 4!'

def test_function_names():
    assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_proper_description():
    README_CONTENT_CHECK_FOR=[]
    functions = inspect.getmembers(session4, inspect.isfunction)
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
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_invalid_function():
    with pytest.raises(AttributeError):
        assert session4.time_it(session4.squared_power_list1, 3,start=0,end=5)
        
def test_exec_without_args():
    with pytest.raises(ValueError):
        assert session4.time_it(print,  sep='-', end= ' ***\n', repetitons=5)
        assert session4.time_it(session4.squared_power_list, start=0,end=5)
        assert session4.time_it(session4.polygon_area, sides = 3, repetitons=10)
        assert session4.time_it(session4.temp_converter, temp_given_in = 'c', repetitons=100)
        assert session4.time_it(session4.speed_converter,  dist='km', time='m', repetitons=200)

def test_exec_without_kwargs():
    with pytest.raises(ValueError):
        assert session4.time_it(print, 1, 2, 3,  repetitons=5)
        assert session4.time_it(session4.squared_power_list, 3)
        assert session4.time_it(session4.polygon_area, 15,  repetitons=10)
        assert session4.time_it(session4.temp_converter, 37.78,  repetitons=100)
        assert session4.time_it(session4.speed_converter, 100,  repetitons=200)

def test_exec_with_str_args():
    with pytest.raises(ValueError):
        assert session4.time_it(print, 'a', sep='-', end= ' ***\n', repetitons=5)
        assert session4.time_it(session4.squared_power_list,'a', start=0,end=5) 
        assert session4.time_it(session4.polygon_area,'a', sides = 3, repetitons=10) 
        assert session4.time_it(session4.temp_converter,'a', temp_given_in = 'c', repetitons=100) 
        assert session4.time_it(session4.speed_converter, 'a', dist='km', time='m', repetitons=200)

def test_check_kwargs_squared_power_list():
    with pytest.raises(ValueError):
        assert session4.time_it(session4.squared_power_list, 3,start1=0,end1=5)

def test_check_kwargs_polygon_area():
    with pytest.raises(ValueError):
        assert session4.time_it(session4.polygon_area, 15, sides2 = 3, repetitons=10)

def test_check_kwargs_temp_converter():
    with pytest.raises(ValueError):
        assert session4.time_it(session4.temp_converter, 37.78, repetitons=100)

def test_check_kwargs_speed_converter():
    with pytest.raises(ValueError):
        assert session4.time_it(session4.speed_converter, 100, dist='km',  repetitons=200)

    
def test_performance_print():
    start1 = time.perf_counter()
    session4.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1

def test_performance_squared_power_list():
    start1 = time.perf_counter()
    session4.time_it(session4.squared_power_list, 3,start=0,end=5)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1

def test_performance_polygon_area():
    start1 = time.perf_counter()
    session4.time_it(session4.polygon_area, 15, sides = 3, repetitons=10)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1

def test_performance_temp_converter():
    start1 = time.perf_counter()
    session4.time_it(session4.temp_converter, 37.78, temp_given_in = 'c', repetitons=100)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1

def test_performance_speed_converter():
    start1 = time.perf_counter()
    session4.time_it(session4.speed_converter, 100, dist='km', time='m', repetitons=200)
    end1 = time.perf_counter()
    delta1 = end1 - start1
    assert delta1 < 0.1

def test_result_squared_power_list():
    assert session4.time_it(session4.squared_power_list, 3,start=0,end=5) == [1, 3, 9, 27, 81, 243], 'squared_power_list is not yielding desired result'
def test_result_squared_power_list_negative():
    assert session4.time_it(session4.squared_power_list, -3,start=0,end=5) == [1, -3, 9, -27, 81, -243], 'squared_power_list is not yielding desired result'

def test_result_polygon_area():
    assert(session4.time_it(session4.polygon_area, 15, sides = 3, repetitons=10)) == 225, 'polygon_area is not yielding desired list'

def test_result_polygon_area_negative():
    with pytest.raises(ValueError):
        assert(session4.time_it(session4.polygon_area, -15, sides = 3, repetitons=10)), 'length / sides cannot be negative'


def test_result_temp_converter():
    assert(session4.time_it(session4.temp_converter, 37.78, temp_given_in = 'c', repetitons=100))==100.004, 'temp_converter is not yielding desired list'
def test_result_speed_converter():
    assert(round(session4.time_it(session4.speed_converter, 100, dist='km', time='m', repetitons=200),2))==1.67, 'speed_converter is not yielding desired list'

def test_result_speed_converter_negative():
    with pytest.raises(ValueError):
        assert(round(session4.time_it(session4.speed_converter, -100, dist='km', time='m', repetitons=200),2))==1.67, 'distance cannot be negative'
