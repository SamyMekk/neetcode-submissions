class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)
        for i in range(n // 2):
            start_pointer = s[i]
            end_pointer = s[n-1-i]
            s[i] = end_pointer
            s[n-1-i] = start_pointer

        """
        Do not return anything, modify s in-place instead.
        """
        