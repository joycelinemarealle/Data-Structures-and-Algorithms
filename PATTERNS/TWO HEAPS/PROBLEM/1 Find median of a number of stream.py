from heapq import *

class MedianOfAStream:

    maxHeap = [] #store first half numbers. We will use negative to simulate max-heap
    minHeap = [] #store second half numbers

    def insert_num(self, num):
       #1 insert either max or min heap
        #if num <= to max element in maxheap then insert to maxheap or else insert to minHeap
        #use negative to show left side of numbers
        #the top element of maxHeap will always be the max
        #check if heap is empty and is max element /top >= num
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        #2 Balance element if odd then decided to have max heap has more element than min heap
        #more element in max heap
        if len(self.maxHeap) > len(self.minHeap)+1:
            heappush(self.minHeap, -heappop(self.maxHeap))

        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    def find_median(self):
        #if we have even number of elements take average of middle two numbers
        if len (self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0]+ self.minHeap[0])/2.0

        #because max heap has one more element
        return -self.maxHeap[0]/1.0


def main():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    print("The median is:" + str(median_of_a_stream.find_median()))

    median_of_a_stream.insert_num(1)
    print("The median is:" + str(median_of_a_stream.find_median()))

    median_of_a_stream.insert_num(4)
    print("The median is:" + str(median_of_a_stream.find_median()))
main()

#Process
#1 Store values < than top element in Max heap. This is heap containing left side of X median.
# balance elements in heap if odd  decided that Max heap has more elements
#2 Store values > than top element in Max heap to Min heap. This heap contains right side of x median
#3 insert a number into heap which takes order big O(log N)
#4 Find average if even take average of top element from both heaps. if odd median is top element of hea






