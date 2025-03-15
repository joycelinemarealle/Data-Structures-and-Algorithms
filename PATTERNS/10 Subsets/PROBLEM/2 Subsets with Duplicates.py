def find_subsets(nums):

    #1 Sort numbers to handle duplicates
    list.sort(nums)
    subsets = []
    subsets.append([]) #2 Create empty set
    startIndex = 0 #
    endIndex = 0 #to track last indexes of subsets before new subsets are added

    #3 loop through element in set
    for i in range(len(nums)):
        startIndex = 0

        #if current nuumber == previous, create new subset from subsets added in previous step
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex +1
        endIndex = len(subsets)-1

        #create a new subset from pre-existing subsets
        for j in range (startIndex, endIndex+1):
            set = list (subsets[j])
            set.append(nums[i])
            subsets.append(set)

    return subsets


def main():
    print( "The list of distinct subsets: " + str(find_subsets([1,3,3])))

main()


#BFS
#sort so as duplicates are next to each other
#start with an empty substet [[]]
#loop through all element in the given set
#ad first element to all pre-existing subset [[], [1]]
        #create a new subset
        # copy prexisting
        #add the current number
# add second element to all pre-existing subsets [[],[1], [3], [1,3]   ]
#add third .............. [[]. [1], [3], [1,3], **[3]**, **[1,3]**,[3,3] [1,3,3]
# if current number == previous, then add current to only subset that were created previously not all pre-existing
#[... [3,3], [1,3,3]]