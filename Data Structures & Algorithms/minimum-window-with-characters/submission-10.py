class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need ={}

        for c in t:
            need[c] = need.get(c,0)+1
        left = 0
        
        have = 0
        window = {}
        need_length = len(need)
        result_length = float('inf')
        result = ''

        for right in range(len(s)):
            char = s[right]
            if char in need:
                window[char] = window.get(char,0)+1
                if window[char] == need[char]:
                    have += 1

            while have == need_length:
                window_length = right - left +1
                if window_length < result_length:
                    result_length = window_length
                    result = s[left:right+1]

                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1
                    if window[left_char] < need[left_char]:
                        have -= 1

                left += 1
        return result

                    

       