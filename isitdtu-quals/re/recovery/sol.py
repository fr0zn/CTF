'''
Reconstruction of a tree from inorder and postorder lists
'''

# POST_ORDER_TMP = []
# INORDER_TMP = []
class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    # def inorder(self):
        # if self.left is not None:
            # self.left.inorder()
        # INORDER_TMP.append(self.key)
        # if self.right is not None:
            # self.right.inorder()

    # def postorder(self):
        # if self.left is not None:
            # self.left.postorder()
        # if self.right is not None:
            # self.right.postorder()
        # POST_ORDER_TMP.append(self.key)

    def __str__(self):
        return "{}, {}, {}".format(self.key, self.left, self.right)


def construct_btree(postord, inord):
    if postord == [] or inord == []:
        return None
    key = postord[-1]
    node = BinaryTree(key)
    index = inord.index(key)
    node.left = construct_btree(postord[:index], inord[:index])
    node.right = construct_btree(postord[index:-1], inord[index + 1:])
    return node



_chall_postorder = [35, 33, 44, 40, 38, 48, 11, 85, 89, 61, 110, 150, 159, 135, 188, 200, 180, 106, 101, 214, 268, 275, 269, 253, 241, 201, 9, 301, 301, 285, 327, 356, 363, 396, 413, 399, 445, 434, 462, 449, 428, 471, 481, 492, 496, 497, 476, 381, 358, 278, 534, 526, 520, 613, 599, 623, 621, 621, 589, 540, 628, 650, 653, 652, 665, 691, 679, 711, 756, 752, 722, 716, 807, 786, 773, 771, 826, 808, 827, 764, 856, 875, 867, 842, 836, 708, 879, 892, 889, 922, 877, 951, 946, 658, 980, 996, 993, 965, 634, 509]
_chall_inorder = [9, 11, 33, 35, 38, 40, 44, 48, 61, 85, 89, 101, 106, 110, 135, 150, 159, 180, 188, 200, 201, 214, 241, 253, 268, 269, 275, 278, 285, 301, 301, 327, 356, 358, 363, 381, 396, 399, 413, 428, 434, 445, 449, 462, 471, 476, 481, 492, 496, 497, 509, 520, 526, 534, 540, 589, 599, 613, 621, 621, 623, 628, 634, 650, 652, 653, 658, 665, 679, 691, 708, 711, 716, 722, 752, 756, 764, 771, 773, 786, 807, 808, 826, 827, 836, 842, 856, 867, 875, 877, 879, 889, 892, 922, 946, 951, 965, 980, 993, 996]

btree = construct_btree(_chall_postorder, _chall_inorder)

# YES, it has spaces between the comas and the values, it took me some time
# to figure this out ...
print "ISITDTU{" + str(btree).replace(', None','') + "}"

