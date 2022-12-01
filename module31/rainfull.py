rainfall_data = []

for i in range( 0, 7 ):
    rainfall_data.append(int(input(f'Please give me {i+1} day rain data : ')))

min_rainfall_value = min(rainfall_data)
max_rainfall_Value = max(rainfall_data)

for i,val in enumerate( rainfall_data ):
    if min_rainfall_value == val :
        print(f'minimum rainfal {i+1} th Day')
        
    if max_rainfall_Value == val :
        print(f'maximum rainfal {i+1} th Day')

