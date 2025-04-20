def containsDuplicate(nums):
    #Create hashmap to store numbers
    numsMaps = set()

    #Iterating through array
    for num in nums:
        #if duplicate return True
        if num in numsMaps:
            return True
        #if not add to set
        numsMaps.add(num)
    return False

def main():
    print(containsDuplicate([1,2,3,3]))
main ()
#Hashmap
#Iterate through nums array
#Check if current element is in hashmap, if it is it a duplicate.so return True
#If not add it to the hashmap
#if finished then return False since no duplicate
#Time complexity O(n) n number of elements
#Memory complexity O(n) number of elements

