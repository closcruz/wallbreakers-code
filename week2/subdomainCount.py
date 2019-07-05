from collections import Counter


class SubdomainVisits:
    def subdomainVisits(self, cpdomains):
        subcount = Counter()

        for d in cpdomains:
            count = int(d.split()[0])
            domains = d.split()[1].split('.')

            for x in range(len(domains)):
                sub = ".".join(domains[x:])

                subcount[sub] += count

        return [str(c) + " " + k for k, c in subcount.items()]


print(SubdomainVisits().subdomainVisits(["9001 discuss.leetcode.com"]))
