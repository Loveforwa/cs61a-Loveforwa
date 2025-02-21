import math

# 定义测量值和权重
measure_value = [
    [9.1, 8.9, 7.6, 9.2, 7.8, 7.9, 8.9, 7.8, 7.9, 7.6, 7.5, 9.0, 9.1, 7.6, 8.9, 9.0, 7.9, 7.6, 9.2, 8.7, 8.9, 8.9, 9.0, 9.1, 9.4, 10, 10, 9.0],
    [7.7, 7.9, 7.9, 9.0, 8.7, 7.9, 8.7, 8.2, 8.7, 8.2, 7.7, 8.9, 9.0, 7.7, 8.7, 8.7, 7.9, 8.7, 9.0, 7.8, 7.9, 8.9, 8.9, 9.2, 8.2, 8.9, 7.9, 10],
    [7.9, 8.9, 8.7, 9.2, 8.9, 8.9, 7.9, 7.9, 8.7, 6.2, 7.9, 8.7, 8.7, 8.7, 7.8, 7.8, 8.9, 8.9, 9.2, 7.9, 8.7, 8.7, 7.8, 7.7, 7.6, 9.3, 9.2, 8.9],
    [8.7, 9.2, 8.7, 9.3, 9.5, 8.7, 8.7, 9.3, 8.7, 7.7, 8.9, 9.7, 9.7, 8.7, 7.9, 8.7, 8.9, 9.2, 9.4, 8.7, 8.9, 9.4, 8.7, 8.7, 9.3, 9.5, 9.6, 8.9]
]

attribute_weights = [0.05, 0.17, 0.20, 0.15, 0.09, 0.09, 0.11, 0.05, 0.09]
sub_attribute_weights = [
    [0.31, 0.36, 0.33],
    [0.33, 0.33, 0.34],
    [0.16, 0.17, 0.17, 0.17, 0.17, 0.16],
    [0.33, 0.34, 0.33],
    [0.34, 0.33, 0.33],
    [0.5, 0.5],
    [0.33, 0.34, 0.33],
    [0.5, 0.5],
    [0.33, 0.33, 0.34]
]

# 初始化结果变量
attributes = [[0] * len(sub_attribute_weights) for _ in range(len(measure_value))]
sub_attributes = [[0] * len(measure_value[0]) for _ in range(len(measure_value))]
final_result = [0] * len(measure_value)
levels = [0] * len(measure_value)

# 功能函数
def power_product_formula(values, weights):
    result = 1.0
    for value, weight in zip(values, weights):
        result *= value ** weight
    return result

def get_level(T, attributes):
    if T >= 9.5 and level_divide(5, attributes):
        return 5
    elif T >= 8.5 and level_divide(4, attributes):
        return 4
    elif T >= 7.0 and level_divide(3, attributes):
        return 3
    elif T >= 4.5 and level_divide(2, attributes):
        return 2
    else:
        return 1

def level_divide(level, attributes):
    count = 0
    flag = True
    if level == 1:
        return True
    elif level == 2:
        for attribute in attributes:
            if attribute < 4.5:
                count += 1
        return count <= 3
    elif level == 3:
        for attribute in attributes:
            if attribute < 7.0:
                count += 1
            if attribute < 4.5:
                flag = False
        return count <= 3 and flag
    elif level == 4:
        for attribute in attributes:
            if attribute < 8.5:
                count += 1
            if attribute < 7.0:
                flag = False
        return count <= 3 and flag
    else:
        for attribute in attributes:
            if attribute < 9.5:
                count += 1
            if attribute < 8.5:
                flag = False
        return count <= 3 and flag

# 计算子属性和主属性值
for i, row in enumerate(measure_value):
    count = 0
    for j, weights in enumerate(sub_attribute_weights):
        values = []
        for x in range(len(weights)):
            sub_attributes[i][count] = row[count]
            values.append(row[count])
            count += 1
        attributes[i][j] = round(power_product_formula(values, weights), 5)

# 计算最终结果和等级
for i in range(len(attributes)):
    final_result[i] = round(power_product_formula(attributes[i], attribute_weights), 3)
    levels[i] = get_level(final_result[i], attributes[i])

# 打印结果
print("子属性值：")
for row in sub_attributes:
    print(row)
print("\n主属性值：")
for row in attributes:
    print(row)
print("\n最终结果：")
print(final_result)
print("\n等级：")
print(levels)
