#loop throught set 
my_set = {10, 20,90 ,30, 30}
for item in my_set:
    print(f"Item: {item}")

#get specific item 
#in Python, sets are unordered, so there’s no "first item" in the traditional
#  sense of a sequence. However, you can convert the set to a list or iterate over 
# it to get an item. Here’s how:
#but u can comvert to list our use iter object 
#⚠️ Note: The order of elements in the set is not guaranteed, so the "first item" may differ each time you run the code.


my_set = {10, 20, 90, 30}
# Get the first item using an iterator
iteratorSet= my_set.__iter__()
print(next(iteratorSet))
print(next(iteratorSet))

# set comperhensice from ist 

listq=[1,2,3,3,4,4,6,7,]

setcomprehensive = {n for n in listq}
print(setcomprehensive)

