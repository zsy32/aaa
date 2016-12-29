import os
import Tree
#11

def ListFilesToTxt(dir, file, wildcard, recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if (os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname, file, wildcard, recursion)
        else:
            for ext in exts:
                if (name.endswith(ext)):
                    file.write(name + "\n")
                    break


def Test():
    dir = "/home/zhenshiziben/pycharm_installation/pdf_to_txt"
    outfile = "hello.txt"
    wildcard = ".txt .exe .dll .lib"

    file = open("/home/zhenshiziben/pycharm_installation/pdf_to_txt/hello1.txt", "r")
    # if not file:
        # print("cannot open the file %s for writing" % outfile)

    # ListFilesToTxt(dir, file, wildcard, 1)
    temp_list = []
    content_list = file.readlines()
    j = 0
    temp = 0
    root = Tree.TreeNode('主题')
    for c in content_list:
        j += 1
        if c.strip()== "内容目录":
            temp = j
            continue
        elif c.strip() == "图表目录":
            break
    print(j)
    print(temp)
    for i in range(temp-1,j-1):
        temp_list.append(content_list[i])
    for t in temp_list:
        print(t[15:40].strip("."))
        print(t[15:40].find(" "))
    level1title1 = Tree.TreeNode(temp_list[1][15:40].strip("."))
    root.add_son(level1title1)
    root.print(show_content=True)

    # str_temp = file.readline()
    # print(temp_list)

    file.close()


Test()
