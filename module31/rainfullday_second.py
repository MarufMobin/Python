All_day = ['Monday', 'Tuesday', 'Wednesday',
           'Thursday', 'Friday', 'Saturday', 'Sunday']
total_rainfall = 0
 
rainfall = {}
 
 
def get_weeks():
    total_weeks = 0
    while True:
        try:
            total_weeks = int(
                input("Enter the number of weeks for which rainfall should be calculated: "))
            if total_weeks < 1:
                print("Number of weeks must be at least 1")
            else:
                break
        except ValueError:
            print("Number of weeks must be an integer.")
 
    return total_weeks
 
 
def get_mm(week_num, day):
    mm = 0
    while True:
        try:
            mm = int(input(
                "Enter the amount of rain (in mm) for {0} of week {1}: ".format(day, week_num)))
            if mm < 0:
                print("Amount of rain must be non-negative")
            else:
                break
        except ValueError:
            print("Amount of rain must be an integer")
 
    return mm
 
 
def avg_weekly_rainfall(weekly_rainfall):
    if len(weekly_rainfall) == 0:
        return 0
    return sum(weekly_rainfall) / len(weekly_rainfall)
 
 
def avg_total_rainfall(weeks):
    avgs = [avg_weekly_rainfall(w) for w in weeks]
    return avg_weekly_rainfall(avgs)
 
 
def get_weekly_rainfall():
    total_weeks = get_weeks()
    total_rainfall = []
 
    for week_num in range(total_weeks):
        weekly_rainfall = [0]*7
        total_rainfall.append(weekly_rainfall)
 
        for i, day in enumerate(All_day):
            weekly_rainfall[i] += get_mm(week_num+1, day)
 
    return total_rainfall
 
 
def print_results(total_rainfall):
    total_weeks = len(total_rainfall)
 
    for week_num in range(total_weeks):
        avg = avg_weekly_rainfall(total_rainfall[week_num])
        weekly_max_min = total_rainfall[week_num]
        print('total weather', weekly_max_min)
        print("Average rainfall for week {0}: {1}".format(week_num+1, avg))
    print("Total average rainfall:", avg_total_rainfall(total_rainfall))
    print('total max wather', max(weekly_max_min))
    print('total min wather', min(weekly_max_min))
 
 
weekly_rainfall = get_weekly_rainfall()
print_results(weekly_rainfall)