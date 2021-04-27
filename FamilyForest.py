global d
d = {}
class FamilyForest:
    def make_family(self, s: str) -> None:
        d[s] = -1

    def union(self, s: str, t: str) -> str:
        parent = ""
        if isinstance(d[s], int) and isinstance(d[t], int):
            wt = d[s] + d[t]
            d[s] = t
            d[t] = wt
            parent = t
        else:
            p1 = self.find(s)
            p2 = self.find(t)
            wt = d[p1] + d[p2]
            if d[p1]>d[p2]:
                d[p1] = p2
                d[p2] = wt
                parent = p2
            else:
                d[p2] = p1
                d[p1] = wt
                parent = p1
        return parent

    def find(self, s: str) -> str:
        if isinstance(d[s], int):
            return s
        else:
            return self.find(d[s])



# f = FamilyForest()
# for s in ["Ricardo", "Sean", "Maya", "Ishaan", "Chia-Lin"]:
#             f.make_family(s)
# f.union("Sean", "Ishaan")
# # f.union("Ricardo", "Chia-Lin")
# # f.union("Maya", "Chia-Lin")

# # f.union("Sean", "Ricardo")
# f.union("Maya", "Ishaan")
# f.union("Ricardo", "Chia-Lin")
# # f.union("Sean", "Ricardo")


# ans = f.find("Chia-Lin")


# print(d)

# print(ans)