# import spog


# def show(index):
#     me = list([[1], [1, 1], []])
#     me_len = len(me)
#     i = 2
#     while(i < me_len and me_len <= index+1):
#         for j in range(0, spog.add(i, 1)):
#             if i < me_len and j <= index+1:
#                 if (j == 0 or j == i):
#                     me[i].append(1)
#                 else:
#                     me[i].append(spog.add(me[i-1][j-1], me[i-1][j]))
#         if (i == me_len-1 and me_len <= index):
#             me.append(list())
#             me_len += 1
#             i += 1
#         else:
#             i += 1
#     return me[index]


# pascal_tree = show(7)

# m = [i for i in pascal_tree]
# print(m)
from PascalTriangle import Pascal as Pascal

p = Pascal(3, "-x", 4)

terms = p.pascalSolution()
p.formatResult(terms)
