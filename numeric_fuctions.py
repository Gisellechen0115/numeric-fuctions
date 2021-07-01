#numeric fuctions 數字函數..

print(min(1,2,3,4,0,2,1))  #to find the minimum of some numbers  #0
print(max([1, 4, 9, 2, 5, 6, 8]))  #to find the maximum of a list #9
print(abs(-99))  #絕對值(absolute value),to find the distance of a number from zero #99
print(abs(42.3)) #42.3
print(sum([1, 2, 3, 4, 5])) #15
#print(sum(1,2,3,4,5))  只對LIST有用

i = 98765.4321
print(round(i))     #98765
print(round(i,1))   #98765.4
print(round(i,2))   
print(round(i,3))


'''
If anyone else is confused about why both 3.5 and 4.5 round to 4 ...

Apparently it's because Python adheres to the IEEE conventions for rounding binary numbers:

https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules

This is different from the convention we learn in school 
(where if it's half-way between two positive numbers, we always round upwards).

Instead it involves "rounding to the nearest number with least significant bit
 equal to 0". For instance, if we are rounding to whole numbers, the least 
 significant digit would be the "ones" or "units" column. For example,
 3 = 11 in binary, 4 = 100 in binary, and 5 = 101 in binary, which respectively 
 have bits 1, 0, and 1 in their right-most "ones" column. So 3.5, being halfway 
 between 3.5 and 4.5, gets rounded to 4 (as it has 0 in the "ones" column, 
 and 3 does not). For the same reason, 4.5 gets rounded to 4, rather than 5.

In case it's relevant, there is a Decimal module which does decimal arithmetic 
precisely (and seems to handle rounding better):

'''
print(round(3.512,2))   #3.51
print(round(3.5))   #4
print(round(4.5))   #4
print(round(-3.4))   #-3
print(round(-3.52))   #-4


print(round(45,-1))   #50
print(round(46,-1))    #40
print(round(34,-1))   #30
print(round(35,-1))   #40
print(round(36,-1))    #40



print(max({i: i*2 for i in range(5)}))
print(max({i: i for i in range(5)}))   #4


a = min([sum ([11, 22]), max(abs(-30), 2)])
b = min(sum ([11, 22]), max(abs(-30), 2))
print(a-b) 


nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

#the fuction enumerate can be used to iterate through the values and indices of a list simultaneously.
# 函數 enumerate 可用於同時迭代列表的值和索引。
for v in enumerate(nums) :  #enumerate列舉
    print(v)
'''
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
'''
for V in enumerate(nums, -3):  #從-3開始做升幕的列表
    print(V)
    

