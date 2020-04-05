class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        length = 0
        longString = ""
        
        for c in s:
            if c in str_list:
                if (len(str_list) > length):
                    length = len(str_list)
                    longString = ''.join(map(str, str_list))
                str_list = str_list[str_list.index(c)+1:]
            str_list += c
        if(len(str_list) > length):
            length = len(str_list)
            longString = ''.join(map(str, str_list))
        return longString

if __name__ == '__main__':
    solution = Solution()
    abc = "hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_string = solution.lengthOfLongestSubstring(abc)
    print(max_string)
    abc = "abcabcdeab"
    max_string = solution.lengthOfLongestSubstring(abc)
    print(max_string)
    abc = "pwwkew"
    max_string = solution.lengthOfLongestSubstring(abc)
    print(max_string)
    abc = ""
    max_string = solution.lengthOfLongestSubstring(abc)
    print(max_string)
    abc = "a va_x uia"
    max_string = solution.lengthOfLongestSubstring(abc)
    print(max_string)