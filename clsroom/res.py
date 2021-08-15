from datetime import date, timedelta

def create_dates(sdate,edate):
    sdate = date(*[int(i)for i in sdate.split(',')])   # start date
    edate = date(*[int(i)for i in edate.split(',')])   # end date
    print(sdate)
    delta = edate - sdate       # as timedelta

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        with open(r"g_class\resources\days.txt","a")as f:
            f.write(',\n'+str(day)+': ')
        print(day)
        
Mtechcs={
"Day-1":["DS","CA","OS-LAB","OS-LAB"],
"Day-2":["OOP","DAA","DS","OS"],
"Day-3":["OS","CA","DAA","AC"],
"Day-4":["DAA","OOP","AA-LAB","AA-LAB"],
"Day-5":["CA","DS","OOP-LAB","OOP-LAB"],
"Day-6":["OOP","DS","OS","AC"]
}
linksmt={
    'OS-LAB':'https://meet.google.com/lookup/gysmi2d4b2',
    'OS':'https://meet.google.com/lookup/f67mr7goeg',
    'OOP':' https://meet.google.com/lookup/bpecf37dx4',
    'DS':'https://meet.google.com/lookup/cqbwumwxii',
    'DAA':'https://meet.google.com/lookup/gm5kc24tch',
    'AA-LAB':'https://meet.google.com/lookup/hhqownlv75',
    'CA':'https://meet.google.com/lookup/gyrebbdgtd',
    'AC':'https://meet.google.com/lookup/b3mrxnc4ts'
}

linkscse3b={
'MES' : 'https://meet.google.com/lookup/drjtqe5rrt?authuser=0&hs=179',
'MES-LAB': 'https://meet.google.com/lookup/b6n5riqe52?authuser=0&hs=179',
'AI' : 'https://meet.google.com/lookup/dolf4bwujq?authuser=0&hs=179',
'AI-LAB': 'https://meet.google.com/lookup/gtmfjssr4l?authuser=0&hs=179',
'OOAD'  :'https://meet.google.com/lookup/dbfwgpvrn2?authuser=0&hs=179',#
'Mini Project' : 'https://meet.google.com/lookup/hq5d6vy37a?authuser=0&hs=179',
'TOC' : 'https://meet.google.com/lookup/eaepkp5z27?authuser=0&hs=179',
'BlockChain' : 'https://meet.google.com/lookup/buvvpfu5cb?authuser=0&hs=179',
'DCN' : 'https://meet.google.com/lookup/h4f3exqgdy?authuser=0&hs=179',
'CN-lab' : 'https://meet.google.com/lookup/cvkrksow2c?authuser=0&hs=179',
'PL':'https://youtube.com/watch?v=dQw4w9WgXcQ'
}

cse3_b1= {
"Day-1": ["MES","PL","TOC","OOAD"],
"Day-2": ["DCN","BlockChain","AI","MES-LAB"],
"Day-3": ["OOAD","TOC","MES","AI"],
"Day-4": ["DON","Mini Project","BlockChain","PL"],
"Day-5": ["TOC","BlockChain","DCN","CN-LAB"],
"Day-6": ["MES","OOAD","AI","AI-LAB"]
    }
cse3_b2={
"Day-1": ["OOAD","PL","AI","DCN"],
"Day-2": ["BlockChain","TOC","DCN","CN LAB"],
"Day-3": ["AI","PE2","DCN","OOAD"],
"Day-4": ["TOC","Mini Project","MES","PL"],
"Day-5": ["MES","BlockChain","A1","AI LAB"]
    }

AIBatch1={
#time  9:30,10:30,1:30,2:30,3:30
"Day-1":["MS","DAA","OOP","FOS","NILL"],
"Day-2":["DBMS","MS","AI","DBMS-LAB","NILL"],
"Day-3":["OOP","FOS","DBMS","MS-LAB","MS-LAB"],
"Day-4":["FOS-LAB","FOS-LAB","OOP","DAA","NILL"],
"Day-5":["AI","DBMS","MS","FOC","MC"],
"Day-6":["sAA","AI","OOP-LAB","OOP-LAB","NILL"]
}
AIBatch2={
"Day-1":["DBMS","OOP","FOS","MS","NILL"],
"Day-2":["DAA","FOS","OOP-LAB","OOP-LAB","NILL"],
"Day-3":["MS","AI","DAA","FOS-LAB","FOS-LAB"],
"Day-4":["DAA","OOP","MS","AI","NILL"],
"Day-5":["MS-LAB","MS-LAB","AI","DBMS","MC"],
"Day-6":["OOP","DBMS","FOS","DBMS-LAB","NILL"],
}

links = {
    'MS':'https://meet.google.com/lookup/bwteimvi63',
    'MS-LAB':'https://meet.google.com/lookup/bwteimvi63',
    'OOP':'https://meet.google.com/lookup/cd272ht2kh',
    'OOP-LAB':'https://meet.google.com/lookup/uut2tetnd',
    'MC':'https://meet.google.com/lookup/hkg5hqdvwn',
    'DBMS':'https://meet.google.com/lookup/cb4snvgebh',
    'DBMS-LAB':'https://meet.google.com/lookup/hwpfjiq774',
    'AI':'https://meet.google.com/lookup/g2yismbr54',
    'DAA':'https://meet.google.com/lookup/hjdxpoh2tm',
    'FOS':'https://meet.google.com/lookup/dfdcf2bhyw',
    'FOS-LAB':'https://meet.google.com/lookup/anksa465tu',
    'NILL':'https://youtube.com/watch?v=dQw4w9WgXcQ'
}

day_order={
"2021-07-29":"Day-4",
"2021-07-30":"Day-5",
"2021-07-31":"Day-6",
"2021-08-01":"Day-0",
"2021-08-02":"Day-1",
"2021-08-03":"Day-2",
"2021-08-04":"Day-3",
"2021-08-05":"Day-4",
"2021-08-06":"Day-5",
"2021-08-07":"Day-0",
"2021-08-08":"Day-0",
"2021-08-09":"Day-6",
"2021-08-10":"Day-1",
"2021-08-11":"Day-2",
"2021-08-12":"Day-3",
"2021-08-13":"Day-4",
"2021-08-14":"Day-0",
"2021-08-15":"Day-0",
"2021-08-16":"Day-5",
"2021-08-17":"Day-6",
"2021-08-18":"Day-1",
"2021-08-19":"Day-2",
"2021-08-20":"Day-0",
"2021-08-21":"Day-0",
"2021-08-22":"Day-0",
"2021-08-23":"Day-3",
"2021-08-24":"Day-4",
"2021-08-25":"Day-5",
"2021-08-26":"Day-6",
"2021-08-27":"Day-1",
"2021-08-28":"Day-0",
"2021-08-29":"Day-0",
"2021-08-30":"Day-0",
"2021-08-31":"Day-2",
"2021-09-01":"Cia-1",
"2021-09-02":"Cia-1",
"2021-09-03":"Cia-1",
"2021-09-04":"Day-0",
"2021-09-05":"Day-0",
"2021-09-06":"Day-6",
"2021-09-07":"Day-1",
"2021-09-08":"Day-2",
"2021-09-09":"Day-3",
"2021-09-10":"Day-0",
"2021-09-11":"Day-0",
"2021-09-12":"Day-0",
"2021-09-13":"Day-4",
"2021-09-14":"Day-5",
"2021-09-15":"Day-6",
"2021-09-16":"Day-1",
"2021-09-17":"Day-2",
"2021-09-18":"Day-0",
"2021-09-19":"Day-0",
"2021-09-20":"Day-3",
"2021-09-21":"Day-4",
"2021-09-22":"Day-5",
"2021-09-23":"Day-6",
"2021-09-24":"Day-1",
"2021-09-25":"Day-0",
"2021-09-26":"Day-0",
"2021-09-27":"Day-2",
"2021-09-28":"Day-3",
"2021-09-29":"Day-4",
"2021-09-30":"Day-5",
"2021-10-01":"Day-6",
"2021-10-02":"Day-0",
"2021-10-03":"Day-0",
"2021-10-04":"Day-1",
"2021-10-05":"Day-2",
"2021-10-06":"Day-3",
"2021-10-07":"Day-4",
"2021-10-08":"Day-5",
"2021-10-09":"Day-0",
"2021-10-10":"Day-0",
"2021-10-11":"Cia-2",
"2021-10-12":"Cia-2",
"2021-10-13":"Cia-2",
"2021-10-14":"Day-0",
"2021-10-15":"Day-0",
"2021-10-16":"Day-0",
"2021-10-17":"Day-0",
"2021-10-18":"Day-3",
"2021-10-19":"Day-0",
"2021-10-20":"Day-4",
"2021-10-21":"Day-5",
"2021-10-22":"Day-6",
"2021-10-23":"Day-0",
"2021-10-24":"Day-0",
"2021-10-25":"Day-1",
"2021-10-26":"Day-2",
"2021-10-27":"Day-3",
"2021-10-28":"Day-4",
"2021-10-29":"Day-5",
"2021-10-30":"Day-0",
"2021-10-31":"Day-0",
"2021-11-01":"Day-6",
"2021-11-02":"Day-1",
"2021-11-03":"Day-2",
"2021-11-04":"Day-0",
"2021-11-05":"Day-3",
"2021-11-06":"Day-0",
"2021-11-07":"Day-0",
"2021-11-08":"Day-4",
"2021-11-09":"Day-5",
"2021-11-10":"Day-6",
"2021-11-11":"Day-1",
"2021-11-12":"Day-2",
"2021-11-13":"Day-0",
"2021-11-14":"Day-0",
"2021-11-15":"Day-3",
"2021-11-16":"Day-4",
"2021-11-17":"Day-5",
"2021-11-18":"Day-6",
"2021-11-19":"Day-1",
"2021-11-20":"Day-0",
"2021-11-21":"Day-0",
"2021-11-22":"Cia-3",
"2021-11-23":"Cia-3",
"2021-11-24":"Cia-3",
"2021-11-25":"Day-0"
}