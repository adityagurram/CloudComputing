import datetime
startDate="20180202"
date_1 = datetime.datetime.strptime(startDate, "%Y%d%m")
for x in range(0, 7):   
    end_date = date_1 + datetime.timedelta(days=x)
    Req_date1=end_date.strftime('%Y%m%d')
    digits1 = [ int(char) for char in str(Req_date1) ]
    TMAX = sum( digits1 )
    Req_date2=end_date.strftime('%Y%m')
    digits2 = [ int(char) for char in str(Req_date2) ]
    TMIN = sum( digits2)
    

