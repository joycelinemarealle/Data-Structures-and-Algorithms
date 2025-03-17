
def subsets(nums):
    subsets = [] #empty list to hold all distinct subsets

    #1 add empty substet
    subsets.append([])
    #2 Loop over the nums
    for currentNumber in nums:
        #3 Get current number of subsets
        n = len(subsets)
        # loop through all existing subset and create new ones
        for i in range(n):
            # create a new subset by copying an existing one and insert current element to it
            set = list(subsets[i])  # copy existing subset
            set.append(currentNumber)  # add current number
            subsets.append(set)  # store new subset

    return subsets
def  main():
    print("All distinct susbsets: " +str(subsets([1,5,3])))


main()
#START WITH empty substet
#loop through elements in subsste
#add first element to all pre-existing subsets
#add second element to all pre-existing subset
#return substets

#start with empty []
# loop through set of elements.
#start with 1 add it all pre-existing elements [], [1]
#add second element to all .... [],[1], [5], [1,5]
#add third element to all ... [],[1], [5], [1,5], [3],[1.3],[1,5,3]