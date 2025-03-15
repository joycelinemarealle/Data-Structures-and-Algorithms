def find_substest(nums):
    subsets= []
    #loop through array of elements
    for currentNumber in nums:
        n = len(subsets)
        #take all existing subsets and insert current number in them to create new subsets
        for i in range (n):
        #create a new subset by copying an existing one and insert current element to it
         set =  list(subsets[i]) #copy existing subset
         set.append(currentNumber) #add current number
         subsets.append(set) #store new subset

    return subsets

def main():
    print("The list of subset is: " + str(find_substest([1,3])))

main()
#give [1,5,3]
#start with empty [[]]
#add first number to existing subsets to create new substes [[],[1]]
#add second number to existing substet to creat new substets [[],[1],[5], [1,5]]
