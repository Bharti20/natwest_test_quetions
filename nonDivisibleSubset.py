def filterSubList(arr, elem, k):
    i = 0
    count = 0
    for i in arr:
        if i != elem:
            sum = i + elem
        if sum% k == 0:
            count = count + 1
    if count>0:
        return False
    else: 
        return True

def main(s, k):
    i = 0
    max_length = 0
    for i in s:
        subarr = []
        subarr.append(i)
        j = 0
        for j in s:
            if i != j:
                sum = i + j
                if sum%k != 0 and  j not in subarr:
                    if len(subarr) > 0:
                        f = filterSubList(subarr, j, k)
                        if f == True:
                            subarr.append(j)
        if len(subarr) > max_length:
            max_length = len(subarr)
    return max_length

listOfNum =  [19, 10, 12, 10, 24, 25, 22]
divisor = 4
print(main(listOfNum, divisor))