class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key string in aphabetical order
        #value will be list
        #return all values
        hashTable = defaultdict(list)

        for word in strs: 
            sortedWord = "".join(sorted(word))
            hashTable[sortedWord].append(word)

        returnList = []
        for sortedWord in hashTable:
            returnList.append(hashTable[sortedWord])

        return returnList