from TravelAgent import TravelAgent 

def main():
    travel_agent = TravelAgent('Zulzana Travel')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC', 'PRA', '05/07/2022')
    print('Aircraft ',trip_info1.aircraft)
    print('Price ', trip_info1.price)

if __name__ == "__main__":
    main()