rainfall_data = []
rainfall_data_total_sum = 0

for i in range( 0, 7 ):
    rain_data = int(input(f'Please give me {i+1} day rain data : '))
    rainfall_data.append( rain_data )
    rainfall_data_total_sum += rain_data


# Find mean and deviation 
rainfall_data_mean = rainfall_data_total_sum / len( rainfall_data )
print(f'The mean is {rainfall_data_mean} ')

# Due work finding deviation
# ----------------

