class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = {}

        for email in emails : 
            local_name, domain_name = email.split("@")
            local_name = "".join(local_name.split("."))
            local_name = local_name.split("+")[0]
            finalEmail = "@".join([local_name, domain_name])
            count[finalEmail] = count.get(finalEmail, 0) + 1

        return len(count) 
