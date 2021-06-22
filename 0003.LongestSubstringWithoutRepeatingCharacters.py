class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxString = ""
        ss = ""
        intMaxString = 0
        rep = False
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if not(s[j-1] in ss):
                    ss = s[i:j]
                    if len(ss) > intMaxString:
                        intMaxString = len(ss)
                        maxString = ss
                else:
                    ss = ""
                    break                    
        #print(intMaxString, maxString)
        return intMaxString
        