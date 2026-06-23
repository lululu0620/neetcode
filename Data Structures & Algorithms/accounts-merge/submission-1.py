class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)

        email_to_name = {}
        # 1. build union
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                parent.setdefault(email, email)
                email_to_name[email] = name
                union(first_email, email)

        # 2. group by root
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        # 3. build result
        res = []
        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name] + sorted(emails))
        return res