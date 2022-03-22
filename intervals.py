N = int(input('No.of intervals: '))
intervals = []
minimum = 0

for i in range(N*2):
    intervals.append(int(input()))

for i in range((N*2)-1):
    if(intervals[i+1] > intervals[i]):
        difference = intervals[i+1] - intervals[i]
        if (i == 0):
            minimum = difference
        if difference < minimum:
            minimum = difference
    else:
        continue
        
print(minimum)