name_list = ["张三", "李四", "王五"]

# 1.取值和取索引
print(name_list[1])
print(name_list.index("王五"))

# 2.修改
name_list[1] = "Jason"
name_list[2] = "Wang"

# 3.增加
# append在末尾位置添加
name_list.append("王小二")
# insert指定索引位置添加
name_list.insert(1, "电放费")
# extend把其它列表追加到当前的列表的末尾
temp_list = ["一", "二", "三"]
name_list.extend(temp_list)

# 4.删除
# remove删除指定数据
name_list.remove("一")
# pop默认状态删除最后的数据，也可指定删除
name_list.pop()
name_list.pop(4)
# clear清除列表数据
name_list.clear()

print(name_list)
