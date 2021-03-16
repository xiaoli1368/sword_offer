#!/bin/bash python
"""
命令行执行并且输出filename，自动在cpp/python文件夹生成两个文件，用法如下：
python test.py "666"
"""
if __name__ == "__main__":
    import os
    import sys
    filename = sys.argv[1]
    path_py = "python/" + filename + ".py"
    path_cpp = "cpp/" + filename + ".cpp"
    if os.path.exists(path_py):
        print("[INFO]: {} has existed".format(path_py))
    else:
        fp1 = open(path_py, "w")
        fp1.close()
        print("[INFO] : success to creat {}".format(path_py))
    if os.path.exists(path_cpp):
        print("[INFO]: {} has existed".format(path_cpp))
    else:
        fp2 = open(path_cpp, "w")
        fp2.close()
        print("[INFO]: success to creat {}".format(path_cpp))
    print("[INFO]: Done")