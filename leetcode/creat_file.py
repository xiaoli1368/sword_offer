#!/bin/bash python
"""
命令行执行并且输出filename，自动在cpp/python文件夹生成两个文件，用法如下：
python test.py "666"
"""
if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	fp1 = open("cpp/" + filename + ".cpp", "w")
	fp2 = open("python/" + filename + ".py", "w")
	fp1.close()
	fp2.close()
	print("Done!")