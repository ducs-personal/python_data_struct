# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self):
        self.data = '#'
        self.l_child = None
        self.r_child = None


class Tree(TreeNode):
    # create a tree
    def create_tree(self, tree):
        data = raw_input('->')
        if data == '#':
            tree = None
        else:
            tree.data = data
            tree.l_child = TreeNode()
            self.create_tree(tree.l_child)
            tree.r_child = TreeNode()
            self.create_tree(tree.r_child)

    # visit a tree node
    def visit(self, tree):
        # 输入#号代表空树
        if tree.data is not '#':
            print str(tree.data) + '\t',

    # 先序遍历
    def pre_order(self, tree):
        if tree is not None:
            self.visit(tree)
            self.pre_order(tree.l_child)
            self.pre_order(tree.r_child)

    # 中序遍历
    def in_order(self, tree):
        if tree is not None:
            self.in_order(tree.l_child)
            self.visit(tree)
            self.in_order(tree.r_child)

    # 后序遍历
    def post_order(self, tree):
        if tree is not None:
            self.post_order(tree.l_child)
            self.post_order(tree.r_child)
            self.visit(tree)

    def travel_btree(self, tree=None, order=None):
        if tree is not None:

            op = {
                'D': lambda: self.visit(tree),
                'L': lambda: self.travel_btree(tree.l_child, order),
                'R': lambda: self.travel_btree(tree.r_child, order),
            }
            for x in order:
                op[x]()

#递归法统计叶子节点的数目：
def count_leaves(tree):
    if tree is None:
        return 0
    if tree.l_child is None and tree.r_child is None:
        return 1
    return count_leaves(tree.l_child)+count_leaves(tree.r_child)

#递归求 二叉树的深度
def depth_btree(tree):
    if tree is None:
        return 0
    else:
        left=depth_btree(tree.l_child)
        right=depth_btree(tree.r_child)
        if left>right:
            return left + 1
        else:
            return right + 1

if __name__ == '__main__':
    #abc##de##f##g##
    t = TreeNode()
    tree = Tree()
    tree.create_tree(t)
    tree.travel_btree(t,"DLR")

    # tree.pre_order(t)
    # print  'pre done'
    # tree.in_order(t)
    # print  'in done'
    # tree.post_order(t)
    # print  'post done'

    print '递归法-统计叶子节点数量'
    print count_leaves(t)


