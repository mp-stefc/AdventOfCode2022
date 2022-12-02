import bisect
cals=[]

with open('input', 'r') as f:
    cur_cal=0
    for line in f:
        l = line.strip()
        if not l:
            bisect.insort(cals, cur_cal)
            cur_cal = 0
        else:
           cal = int(l) 
           cur_cal = cur_cal + cal

top3 = cals[-3:];
res = sum(top3)
print("Highest single calories value: " , cals[-1])
print("Highest three calories combined: ",  sum(top3))
