class Interval:
    def __init__(self, start,end):
        self.start = start
        self.end = end
    def print_interval(self):
        print( "[" + str(self.start) + " " + str(self.end) + " ]")

def merge(intervals):
    #edge case if only one interval
    if len(intervals) <2:
        return intervals
    #sort intervals on start time a.start <= b.start
    intervals.sort( key = lambda x : x.start)

    mergedIntervals = []

    #if a overlaps b meaning b.start<= a.end
    start = intervals[0].start
    end = intervals[0].end

    #Iterate through each interval
    for i in range(1, len(intervals)): #start at 1 because using first element as a for reference above
        #check if a overlaps b
        interval = intervals[i]
        if interval.start <= end:
            end = max(end, interval.end)
        else: #non overlapping add previous interval
             mergedIntervals.append(Interval(start,end))
             start = interval.start
             end = interval.end
    #add the last interval
    mergedIntervals.append(Interval(start,end))
    return mergedIntervals

def main():
    print("Merged intervals: " , end = ' ')
    for i in  merge([ Interval(1,4), Interval(2,5), Interval(7,9) ]):
        i.print_interval()
    print()
main ()
#sort the intervals by start element #if a.start <== b.start
#if a overlaps  b b.start <= a.end --> we merge into new interval
    #c.end= max(a.end and b.emd
#keep repeating two steps if next intervals overlaps with c