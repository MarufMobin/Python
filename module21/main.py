from TravelAgent import TravelAgent 

def main():
    travel_agent = TravelAgent('Zulzana Travel')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '05/07/2022')
    # print('Aircraft ',trip_info1.aircraft)
    # print('Price ', trip_info1.price)

    trip_cities = ['DUB', 'ORD' , 'LHR','SYD','JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route( trip_cities, '05/11/2022')
    
    print('Trip Price ', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)


if __name__ == "__main__":
    main()