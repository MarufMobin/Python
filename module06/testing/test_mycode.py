import my_code

api_link = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

def test_getresponse():
    ret = my_code.get_response(api_link)
    print(ret)
    print(ret.status_code)
    assert ret.status_code == 200

# test_getresponse() 

def test_sum():
    assert 3 == 3

    