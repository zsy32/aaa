__author__ = 'shiotoli'
class TreeNode:

    def __init__(self,title = 'XXX'):
        self.title = title
        self.is_leaf = True
        self.children = []
        self.content = ''
        self.father = None

    def add_son(self,son):
        son.father = self
        self.children.append(son)
        self.is_leaf = False

    def set_content(self,content):
        if not self.is_leaf:
            print('content cannot save in non-leaf node')
            return
        self.content = content


    def print(self,level=0,show_content = False):
        if self.is_leaf:
            str = ''
            for i in range(level):
                str += '\t'
            print(str+'title:'+self.title+'(leaf)')
            if show_content:
                print(str+'content:'+self.content+'\n')
            else:
                print('\n')
        else:
            str = ''
            for i in range(level):
                str += '\t'
            print(str+'title:'+self.title+'\n')
            for son in self.children:
                son.print(level+1,show_content)


