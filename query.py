import json

# 从文件中读取嵌套字典
with open('nested_region_code_with_fullname.json', 'r', encoding='utf-8') as f:
    nested_dict = json.load(f)

# 递归搜索函数
def search_region(target, d):
    for key, value in d.items():
        if key.startswith(target):
            return value.get('adcode', '未找到对应的 adcode')
        sub_dict = value.get('下属区划')
        if sub_dict:
            result = search_region(target, sub_dict)
            if result:
                return result
    return None

# 获取用户输入
x = input("请输入你要查询的地区：")

# 进行搜索
adcode = search_region(x, nested_dict)

# 输出结果
if adcode:
    print(f"你要查询的地区是：{x}，对应的 adcode 是：{adcode}")
else:
    print(f"未找到与 '{x}' 相关的地区")
