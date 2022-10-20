txt = "my name is maruf mobin"

def make_upper( txt ):
    return (txt.upper())

def make_lower( txt ):
    return (txt.lower())

def make_capital( txt ):
    return (txt.capitalize())

def function_called( txt ):
   print( make_capital( txt ) )
   print(make_lower( txt ))
   print( make_upper( txt ) )
    
if __name__ == '__main__':
    function_called( txt )

