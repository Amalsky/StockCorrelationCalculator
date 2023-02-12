import csv
import statistics

# variable name "bench_mark represent the bench mark index or stock "
#csvfile for this particular analyze is= [nifty,1year,daily.csv,ADANIENT.1year,daily.csv]




with open('nifty,1year,daily.csv') as bench_mark, open('ADANIENT.1year,daily.csv ') as stock_name:
    std_stock=[]
    def corerelation(dataz,price): # Finding daily returns
        bench_mark_daily_return = []
        bench_mark_dispersion = []
        stock_name_daily_return = []
        index1 = 0
        index_for_dispersion = 0
        stock1 = price
        stock1_avarage_daily_return = 0
        data = csv.reader(dataz)
        data.__next__()
        for line in data:

            if index1 >= 1:
                closing = ''.join(line[4])
                closing = float(closing)

                daily_return = closing / stock1 - 1

                bench_mark_daily_return.append(daily_return)
                # Finding avrage return
                stock1_avarage_daily_return = sum(bench_mark_daily_return) / len(bench_mark_daily_return)
                stock1_avarage_daily_return = stock1_avarage_daily_return
                stock1 = closing
            index1 += 1
        # Finding dispirtion
        for line in bench_mark_daily_return:
            dispersion = bench_mark_daily_return[index_for_dispersion] - stock1_avarage_daily_return
            bench_mark_dispersion.append(dispersion )
            index_for_dispersion += 1

        #finding std
        std=statistics.stdev(bench_mark_daily_return)
        std_stock.append(std*15.8113883)
        return bench_mark_dispersion

    #corretion
    def co(dataset1,data2):
        index=0
        dispertion_multiplyer=[]
        for line in dataset1:
            result=line*data2[index]
            result=result*100
            index+=1
            dispertion_multiplyer.append(result)
        count=len(dispertion_multiplyer)-1
        covariance=sum(dispertion_multiplyer)/count
        covariance=covariance
        s=std_stock[0]*std_stock[1]
        corrreation=covariance/s
        return corrreation





    #calling the function   (16955.44922,1658.09976) is the opening price

    print(co(corerelation(bench_mark, 16955.44922), corerelation(stock_name, 1658.099976)))


















