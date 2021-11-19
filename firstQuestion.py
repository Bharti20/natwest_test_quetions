def birthdayCakeCandles(listOfCandles):
    count = 0
    max_height = max(listOfCandles)
    index = 0
    while index < len(listOfCandles):
        if listOfCandles[index] == max_height:
            count = count + 1
        index = index + 1
    return count

candles = [4, 4, 1, 3]
print(birthdayCakeCandles(candles))