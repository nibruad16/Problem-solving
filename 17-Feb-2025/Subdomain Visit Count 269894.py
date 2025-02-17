# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for time_domain in cpdomains:
            time = int(time_domain[:time_domain.index(' ')])
            subdomain = time_domain[time_domain.index(' ')+1:]
            cnt[subdomain]+=time
            for ind,char in enumerate(subdomain):
                if char =='.':
                    cnt[subdomain[ind+1:]]+=time
        return [str(time)+" " + domain for domain, time in cnt.items()]