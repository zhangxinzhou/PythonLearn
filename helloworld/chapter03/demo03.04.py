print("\n为了您和他人的安全,严禁酒后开车")
proof = int(input("请输入美100毫升血液酒精的含量"))
if proof < 20:
    print("您还不构成饮酒行为,可以开车,但要注意安全")
else:
    if 20 <= proof < 80:
        print("\n已经达到酒后驾驶标准,请不要开车")
    else:
        print("\n已经达到醉酒驾驶标准,千万不要开车")

