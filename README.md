# Birthday Cake Candles 

### I wrote this code to find the tallest candle from the list,
### For that, there are two steps:
#####  1. Using the max method I am finding the tallest candle from the list
#####  2. and then I applied a loop to count the duplicates of the tallest candle then returning the count of the duplicates



# Non Divisible Subset 

### There are two functions –
##### 1. filterSublist
##### 2. main function

### This is how I applied my logic-
#### S = [19, 10, 12, 10, 24, 25, 22],  k = 4
##### S[0] = [19, 10, 12, 24, 22]
######     = [19, 10, 12, 24]
######     = [19, 10, 12]
##### S[1] = [10, 12, 24, 25]
######     = [10, 12, 25]
##### S[2] = [12, 10, 25, 22]
######     = [12, 10, 25]
##### S[3] = [10, 25]
##### S[4] = [24, 25, 22]

#### So the first function “filterSublist” is to filter the subset each time getting created. “filterSublist” is to not let an element push in the sublist, if the element is duplicate or evenly divisible by the sum of the element and anyone of sublist element. With the help of this function I will get a filtered sublist as explained above.

### In the main function
#### I have a variable called “max_length” = this variable is basically to get the length of highest subset.


