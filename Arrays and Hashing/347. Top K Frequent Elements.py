class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Approach: 
        A map to count the repetitions, A list of lists of size len(nums)+1 to record the nums of repetations, ex: list[3] = 3xRepeated-element, finally iterate the list of lists from end and store the ele in newList until newList size == k
        time: O(n+n+n) = O(n)
        """

        count = {}
        freq = [[] for i in range(len(nums)+1)]     # we can have a max repetitions of len(nums)+1 thats why the length of the freq list will match it

        for n in nums:                              # iterate the list and count the repetitions and store it as val
            count[n] = 1 + count.get(n, 0)     
        
        for key, val  in count.items():             # consider index of freq as the repetitions and append key(num) to index --- ex: freq[3] = (value of 3xRepeated-element)
            freq[val].append(key)
        
        res = []                                    
        for i in range(len(freq) - 1, 0, -1):       # iterate from the last element backwards
            for n in freq[i]:                       # since freq is a list of list, there might be multiple elements with same repetitions... they will be stored in the same index
                res.append(n)
                if len(res) == k:                   # we are asked to return only the most frequest 'k' elements, so when we have 'k' elements we end
                    return res
