class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ### Remove each item of s from t, after this,
        ### if t is emty strings are anagram else not anagram
        # if len(s) != len(t):
        #     return False
        # for i in s:
        #     t = t.replace(i, "", 1)

        # if not t:
        #     return True
        # else:
        #     return False

        ### Push each element of s in arr then remove each element of t from arr
        ### if arr is emty strings are anagram else not anagram
        if len(s) != len(t):
            return False
        arr = []
        for i in s:
            arr.append(i)
        for i in t:
            arr.remove(i) if i in arr else None
        if not arr:
            return True
        else:
            return False
            
        