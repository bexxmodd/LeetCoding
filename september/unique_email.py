class Solution:
    def numUniqueEmails(self, emails) -> int:
        dictionary = set()
        for email in emails:
            name, domain = email.split("@")
            wild_card = name.split("+")[0]
            new_name = ''.join(st for st in wild_card.split('.'))
            combined_name = new_name + '@' + domain
            dictionary.add(combined_name)
        return len(dictionary)


s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))