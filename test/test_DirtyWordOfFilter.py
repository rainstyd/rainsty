# test_DirtyWordOfFilter.py

from Algorithm.DirtyWordOfFilter import DFAFilter
import time


def main():
    time1 = time.time()
    gfw = DFAFilter()
    text = "你真是个大傻逼，大傻子，傻大个，大坏蛋，坏人。"
    result = gfw.filter(text)

    print(text)
    print(result)
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')


if __name__ == '__main__':
    main()
