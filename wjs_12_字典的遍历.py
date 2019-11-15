xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "QQ": 123456789}

# 迭代遍历字典
# c是每次循环中获得的KEY

print(xiaoming["QQ"], "+++")

for c in xiaoming:
    print("%s - %s" % (c, xiaoming[c]))
