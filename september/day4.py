class Solution:
    def partitionLabels(self, S: str) -> list:
        labels = []

        [ord(char) - 97 for char in raw_input('Write Text: ').lower()]

sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))