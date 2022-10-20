import pytest
import sample

txt = "my name is maruf mobin"
 
def make_upper():
    assert txt.upper() 

def make_capital():
    assert txt.capitalize()

def make_lower():
    assert txt.lower()

