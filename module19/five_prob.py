space_invaders = [...]  # Global Variable
player_pos = ( 200 , 25 ) # Global Variable 
max_level = 10 # Global variable

def play ( ) : # Function Variable 
    level = 1 # Local Variable / loop initializer 
    while ( level < max_level +1 ) :
         if len ( space_invaders ) == 0 : 
            level += 1 
            continue 
        