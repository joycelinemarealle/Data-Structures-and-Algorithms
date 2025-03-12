from heapq import *
class medianOfNumberStream():

    maxHeap= [] #store -ve elements
    minHeap=[]

    def insertNum(self, num):

        #Insert number two max heap if maxHeap empty or num <= to top element [0]
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap,-num)

        elif -self.maxHeap[0] < num:
            heappush(self.minHeap, num)

        #Balance elements across heap, if odd then maxHeap holds more element
        if len(self.maxHeap)> len(self.minHeap) +1:
               heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush (self.maxHeap, - heappop(self.minHeap))

    def findMedian(self):
        #if len is same then average sum of top elements/2
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0])/2.0

        #else odd then return top element of maxHeap
        return -self.maxHeap[0]


def main():
    median_Of_Number_Stream = medianOfNumberStream()
    median_Of_Number_Stream.insertNum(1)
    print ("The median is "+str(median_Of_Number_Stream.findMedian()))

    median_Of_Number_Stream.insertNum(3)
    print ("The median is "+str(median_Of_Number_Stream.findMedian()))
    median_Of_Number_Stream.insertNum(5)
    print ("The median is "+str(median_Of_Number_Stream.findMedian()))


main()










#Two heap method to keep track of the numbers max  has left sidev& called finding the max element amd min
#insert elements in max or min heap. Check if the num <= to top element of max heap, then add it. if not i add to min heap
 # in max heap, i will save -ve numbers

# Balance elements in both heaps. if total is odd, decided to keep more element in the max heap
# find median ( if even find average of top elements of both max and min heap) if not then find top element of max heap