class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        Approach:
        Map each (string element)value to (list of char)key (key = list of char in each str, value = elements of strs)
        1) create hashmap with defaultdict(list)
        2) iterate through strs and create alpha-counter(list) for each str, iterate through str for each char and store in alpha-counter
        3) append the current str to list and finally return only the values
        """
        res = defaultdict(list)                     # create hashmap/if the key doesnt exist, it creats a new key with empty value(list)
                                                    # absolutely necessary when using append, 
        for s in strs:
            count = [0] * 26                        # consider 0 = a ... 25 = z

            for c in s:
                count[ord(c) - ord("a")] += 1       # fetch the ascii value of current char and subtract ascii of "a" for locating index
                                                    # then increment the value at the index
            res[tuple(count)].append(s)             # we cannot have lists as keys for hashmap so we use tuple and append the str to count
        
        return res.values()                         # we dont require the keys anymore so we return values which is List[List[str]] by default
