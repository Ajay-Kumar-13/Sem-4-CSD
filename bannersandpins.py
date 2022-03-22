B = int(input('Number of Banners: '))
bannerLengths = []
pin = 0
for i in range(B*2):
    bannerLengths.append(int(input('Enter Length: ')))
banners = []
for i in range((B*2)-1):
    if i%2==0:
        start = bannerLengths[i]
        end = bannerLengths[i+1]
        banners.append([start, end])
j = 0
size = len(bannerLengths)
while(size):
    if banners:
        length = bannerLengths[j]
        if bannerLengths.count(length) > 1:
            pin += 1
            size -= bannerLengths.count(length)
            for element in bannerLengths:
                if element == length:
                    bannerLengths.remove(element)
            i = 0
            while(B != i):
                if length in banners[i]:
                    banners.remove(banners[i])
                    B -= 1
                    i = 0
                else:
                    i += 1
            j = 0
        else:
            j += 1
    else:
        break
        
pin = pin+len(banners)

print(pin)