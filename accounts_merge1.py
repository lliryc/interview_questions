from typing import List, Dict, Set

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Merges accounts with common email addresses.

        Args:
        accounts (List[List[str]]): A list of accounts, where each account is represented as a list
                                    with the first element being the account name and the remaining
                                    elements being email addresses.

        Returns:
        List[List[str]]: A list of merged accounts, each represented as a list with the account name
                         followed by the sorted list of unique email addresses.
        """
        
        # Map from account index to account name
        ids: Dict[int, str] = {i: accounts[i][0] for i in range(len(accounts))}
        # Map from account index to set of email addresses
        ids_mails: Dict[int, Set[str]] = {i: set(accounts[i][1:]) for i in range(len(accounts))}
        # Map from email address to account index
        mails: Dict[str, int] = {}
        # List of account indices
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
                    elif mail not in mails:
                        mails[mail] = i

        # Prepare the result list
        res = []
        for i in ids:
            line = [ids[i]] + sorted(ids_mails[i])
            res.append(line)
        
        return res

# Example usage:
s = Solution()

# Test cases
accounts1 = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"]
]

accounts2 = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]

# Running tests
print(s.accountsMerge(accounts1))
# Output: [['David', 'David0@m.co', 'David1@m.co', 'David2@m.co', 'David3@m.co', 'David4@m.co', 'David5@m.co']]

print(s.accountsMerge(accounts2))
# Output: [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']]
