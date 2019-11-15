# 使用多个键值对，存储描述一个`物体`的相关信息——
# 描述更复杂的数据信息将多个字典放在一个列表中，
# 再进行遍历，在循环体内部针对每一个字典进行相同的处理

card_list = [
    {"name": "Jason",
     "age": 18,
     "height": 1.75},
    {"name": "小明",
     "age": 21,
     "height": 1.85}
]

for card_list in card_list:
    print(card_list)
