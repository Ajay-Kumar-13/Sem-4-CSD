N = int(input('Enter N: '))
coordinates=[]
distances = []
for i in range(N):
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    coordinates.append([x1, y1])
    
for i in range(N-1):
    if coordinates[i][0] > coordinates[i+1][0]:
        x = coordinates[i][0] - coordinates[i+1][0]
    else:
        x = coordinates[i+1][0] - coordinates[i][0]
        
    if coordinates[i][1] > coordinates[i+1][1]:
        y = coordinates[i][1] - coordinates[i+1][1]
    else:
        y = coordinates[i+1][1] - coordinates[i][1]
        
    sum = x + y
    
    distances.append(sum)
    
Sum = 0
for element in distances:
    Sum = Sum + element
    
print(Sum)