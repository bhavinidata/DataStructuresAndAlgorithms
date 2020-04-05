class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

# Faster in 116ms
        str_list = []
        length = 0      
        for c in s:
            if c in str_list:
                if (len(str_list) > length):
                    length = len(str_list)
                str_list = str_list[str_list.index(c)+1:]
            str_list += c
        if(len(str_list) > length):
            length = len(str_list)
        return length

if __name__ == '__main__':
    solution = Solution()
    abc = "hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length: {max_length}")
    abc = "bbbbb"
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length: {max_length}")
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length: {max_length}")
    abc = "pwwkew"
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length: {max_length}")
    abc = ""
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length at the last: {max_length}")
    abc = " "
    max_length = solution.lengthOfLongestSubstring(abc)
    print(f"Max length: {max_length}")

    # Longer time
        # pos_map = {}
        # # s = s.lower()
        # if not s:
        #     return 0
        # max_len = 0
        # for i in range (len(s)):
        #     # Handle last letter
        #     if i == len(s)-1:
        #         if s[i] not in pos_map:
        #             max_len += 1
        #         # print(f"Max length at the last char: {max_len}")
        #         return max_len
        #     pos_map.clear()
        #     pos_map[s[i]] = i
        #     curr_len = 1
        #     j=0
        #     for j in range (i+1, len(s)-j):
        #         # print("in second for loop")
        #         # print(f"Initial Current Length: {curr_len}")
        #         # print(s[j])
        #         # handle last letter
        #         if j == len(s)-1:
        #             if s[j] not in pos_map:
        #                 curr_len += 1
        #             if max_len < curr_len:
        #                 max_len = curr_len
        #             # print(f"Max length at the last char: {max_len}")
        #             return max_len
        #         # Handle duplicates
        #         if s[j] in pos_map:
        #             # print("found match!")
        #             if max_len < curr_len:
        #                 max_len = curr_len
        #             # print(f"Max Length: {max_len}")
        #             # print(f"Current Length: {curr_len}")
        #             curr_len = 1
        #             break
        #         else:
        #             pos_map[s[j]] = j
        #             curr_len +=1
        # return max_len

        # dicts = {}
        # maxlength = start = 0
        # for i,value in enumerate(s):
        #     if value in dicts:
        #         sums = dicts[value] + 1
        #         if sums > start:
        #             start = sums
        #     num = i - start + 1
        #     if num > maxlength:
        #         maxlength = num
        #     dicts[value] = i
        # return maxlength