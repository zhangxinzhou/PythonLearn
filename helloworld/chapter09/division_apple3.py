def division():
    '''功能:分苹果'''
    print("\n===================分苹果了====================\n")
    apple = int(input("请输入苹果的个数:"))
    children = int(input("来个几个小朋友:"))
    assert apple > children, "苹果不够分"
    result = apple // children
    remain = apple - result * children
    if remain > 0:
        print(apple, "个苹果,平均分给", children, "个小朋友,每人分", result, "个,剩下", remain, "个")
    else:
        print(apple, "个苹果,平均分给", children, "个小朋友,没人分", result, "个")


if __name__ == '__main__':
    division()
