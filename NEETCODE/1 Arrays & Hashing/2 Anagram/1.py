def isAnagram(s,t):
     #Check length of strings
    if len(s) != len(t):
        return False
    #Create empty maps
    sMap = {}
    tMap ={}
    #Iterate through one string & update counts in Hashmaps
    for i in range(len(s)):
        sMap[s[i]]= 1+ sMap.get(s[i],0)
        tMap[t[i]]= 1+ tMap.get(t[i],0)
    #Iterate through maps and compare the count
    for char in sMap:
        if sMap[char] != tMap.get(char,0): #if key does not exist set default
            return False
    return True

def main ():
    s = 'racecar'
    t = 'carrace'
    print(isAnagram(s,t))
main()
#Anagram same length and the count per char is same
# will have input with non alphabetical char eg race..care
#Check if length if not the same return False
#sMap and tMap key:value char:count
#Iterate through one of string and update the  count of char of both s and t
#Iterate through the oneMap and compare the count of char. if not same return False
#return True if valid
#Time complexity O(n) n number of elements
#Memory complexity O(n) length of s
