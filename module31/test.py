import halfadder

def test_get_print_result():
    ret = halfadder.get_print_result( 0, 1 )
    assert( ret[0] == 1 and ret[1] == 0 ) 

