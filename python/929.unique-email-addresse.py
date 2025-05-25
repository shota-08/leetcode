# [929] Unique Email Addresse

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            # find "@"
            di = email.find("@")
            local = email[:di]
            domain = email[di:]

            # find "+"
            pi = local.find("+")
            if pi != -1:
                local = local[:pi]

            # find "."
            local = local.replace(".", "")

            comp = local + domain
            uniques.add(comp)

        return len(uniques)