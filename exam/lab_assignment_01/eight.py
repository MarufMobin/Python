# import file name

name = "i love python"

def make_upper():
    return (name.upper())

def make_capital():
    return (name.capitalize())

def make_lower():
    return (name.lower())

def test_script():
    assert make_upper()
    assert make_capital()
    assert make_lower()
