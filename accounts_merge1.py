from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ids = {i: accounts[i][0] for i in range(len(accounts))}
        ids_mails = {i: set(accounts[i][1:]) for i in range(len(accounts))}
        mails = {}
        acc_list = list(ids.keys())
        for i in acc_list:
            mail_list = list(ids_mails[i])
            merged = True
            while merged:
                merged = False
                for mail in mail_list:
                    if mail in mails and mails[mail] != i:
                        merged = True
                        old_i = mails[mail]
                        old_mails = ids_mails[old_i]
                        ids_mails[i] = ids_mails[i].union(old_mails)
                        del ids[old_i]
                        del ids_mails[old_i]
                        for mail in old_mails:
                            mails[mail] = i
                    elif not mail in mails:
                        mails[mail] = i
        res = []
        for i in ids:
            line = [ids[i]] + list(sorted(ids_mails[i]))
            res.append(line)
        return res
s = Solution()
print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))