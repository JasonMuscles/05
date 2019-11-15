name_list = ["张三", "李四", "王五", "张三"]

# len 函数可以统计列表中的元素总数
list_len = len(name_list)
print(list_len)

# count方法可以统计列表中的某一个数据的次数
count = name_list.count("张三")
print(count)

# 从列表中删除数据
name_list.remove("张三")
print(name_list)
