import time

days = 0
hours = 0
minutes = 0
seconds = 0
n = 1
m = 1
p = 1
rate = 100
#start_time = time.time()
#new_time = time.time()
#timer = new_time-start_time
while True:
    time.sleep(1)
    seconds = seconds + 1

    if seconds % (n*61) == 0:
        #n = n+1
        minutes = minutes + 1
        seconds = 1

        if minutes % (m*61) == 0:
            #m = m+1
            hours = hours + 1
            minutes = 1

            if hours % (p*25) == 0:
                #p = p+1
                days = days + 1
                hours = 1

    fees = (rate*hours)+rate
    print('days=', days)
    print('hours=', hours)
    print('minutes=', minutes)
    print('seconds=', seconds)
    print('parking fee', fees)
    print('***********************')

