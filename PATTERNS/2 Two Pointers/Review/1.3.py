def pair_with_target_current_sum(arr, target):
    left = 0
    right = len(arr)-1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left,right]
        if current_sum > target:
           right -=1
        else:
            left +=1
    return [-1,-1]

def main():
    print(pair_with_target_current_sum([1,2,3,4,6], 6))

main()

#two pointer one from left and one right
    #while loop while left < right
            #arr[left] + arr[right] = current_current_sum
    #check if current_current_sum > = target
    #if greater then move right pointer left
    #if smaller move left pointer right
    #if equal return [left, right]