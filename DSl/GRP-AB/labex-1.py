
cric_list = []
bad_list = []
foot_list = []

num_1 = int(input("No. of Cricket Players- "))
for i in range(0, num_1):
    n1 = int(input("Roll No. - "))
    if n1 not in cric_list:
        cric_list.append(n1)

num_2 = int(input("No. of Badminton Players- "))
for i in range(0, num_2):
    n1 = int(input("Roll No. - "))
    if n1 not in bad_list:
        bad_list.append(n1)

num_3 = int(input("No. of Football Players- "))
for i in range(0, num_3):
    n1 = int(input("Roll No. - "))
    if n1 not in foot_list:
        foot_list.append(n1)

print("Cricket List-", cric_list)
print("Badminton List-", bad_list)
print("Football List-", foot_list)


def intersection(lst1, lst2):
    l1il2 = []
    if len(lst1) >= len(lst2):
        for i in lst1:
            for j in lst2:
                if i == j:
                    l1il2.append(i)
        return l1il2
    elif len(lst1) <= len(lst2):
        # l1il2 = []
        for i in lst2:
            for j in lst1:
                if i == j:
                    l1il2.append(i)
        return l1il2


def union(lst1, lst2):
    if len(lst1) >= len(lst2):
        lstu = lst2
        for i in lst1:
            if i not in lstu:
                lstu.append(i)
            else:
                pass
        return lstu
    else:
        lstu = lst1
        for i in lst2:
            if i not in lstu:
                lstu.append(i)
            else:
                pass
        return lstu


def subtracter(lst1, lst2):
    if len(lst1) >= len(lst2):
        lstsub = lst1
        for i in lst2:
            if i in lst1:
                lstsub.remove(i)
            else:
                pass
        return lstsub
    else:
        lstsub = lst2
        for i in lst1:
            if i in lst2:
                lstsub.remove(i)
            else:
                pass
        return lstsub


# print()
print("A)", intersection(cric_list, bad_list))
print("B)", subtracter(intersection(cric_list, bad_list), union(cric_list, bad_list)))
print("C)", subtracter(foot_list, union(intersection(foot_list, cric_list), intersection(foot_list, bad_list))))
print("D)", subtracter(union(cric_list, foot_list),
                       union(intersection(cric_list, bad_list), intersection(bad_list, foot_list))))
