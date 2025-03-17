def subsets(nums):
    subsets = [] # a list to hold subsets

    # start with an empty []
    subsets.append([])
    #loop through the numbs and add element to @ pre exisitng subsets
    for currentNumber in nums:
        for i in range (len(subsets)):
            #create new subset when adding element to each prexisitng subset
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set) #add new subset to old subsets
    return subsets


def main():
    print("The subsets are: " + str(subsets([1,3])))
main()




#disntic element no duplicate
#results [1,3] == [3,1] only one of it
#BFS
#initialize an empty [[]]
#loop through the set and add @ element to all pre existing subsets by create a new subset. then appending this subset to original set
# [[]]
#  take 1 and add it all pre existing subset [[], [1]]
#take 2 element and add to .... [[],[1], [3],[1,3]]