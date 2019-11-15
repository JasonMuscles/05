name_list = ["张三", "李四", "王五"]

# * 使用 `del` 关键字(`delete`) 同样可以删除列表中元素
del name_list[1]
# * `del` 关键字本质上是用来 **将一个变量从内存中删除的
name = "小李"
# * 如果使用 `del` 关键字将变量从内存中删除，
# 后续的代码就不能再使用这个变量了
print(name)

del name

print(name_list)
