#Statistics Killer v0.1 by Entity 303

from collections import Counter
import msvcrt

# 计算平均数
def calculate_mean(numbers):
    # 计算平均值
    mean = sum(numbers) / len(numbers)

    # 返回计算结果
    return mean

# 计算中位数
def calculate_median(numbers):
    # 对列表进行排序
    sorted_numbers = sorted(numbers)
    
    # 获取列表长度
    length = len(sorted_numbers)
    
    # 判断列表长度的奇偶性
    if (length % 2 == 0):
        # 对于偶数长度的列表，中位数为中间两个数的平均值
        mid_index_1 = length // 2
        mid_index_2 = mid_index_1 - 1  # 之所以是减一不是加一是因为列表索引是从0开始，因此 length // 2 刚好是 后一个数，减去一刚好是前一个数
        median = (sorted_numbers[mid_index_1] + sorted_numbers[mid_index_2]) / 2
    else:
        # 对于奇数长度的列表，中位数为中间的数
        mid_index = length // 2
        median = sorted_numbers[mid_index]
    
    # 返回计算结果
    return median

# 计算众数
def calculate_mode(numbers):
    # 使用Counter计算每个数的出现频率
    frequency = Counter(numbers)
    
    # 获取出现频率最高的数值列表
    mode_values = frequency.most_common()
    
    # 获取最高频率
    max_frequency = mode_values[0][1]
    
    # 获取所有最高频率的数值
    modes = [value for value, freq in mode_values if freq == max_frequency]
    
    # 返回计算结果
    return modes

# 计算方差
def calculate_variance(numbers, mean):
    # 计算每个数与平均值的差的平方
    squared_diff = [(x - mean) ** 2 for x in numbers]
    
    # 计算差的平方的平均值
    variance = sum(squared_diff) / len(numbers)
    
    # 返回计算结果
    return variance

def main():
    # 获取输入的一组数
    input_numbers = input("请输入一组数（以空格分隔）：").split()

    # 转换为数字列表
    numbers = [float(x) for x in input_numbers]

    # 计算平均数
    mean = calculate_mean(numbers)
    # 计算中位数
    median = calculate_median(numbers)
    #计算众数
    modes = calculate_mode(numbers)
    # 计算方差
    variance = calculate_variance(numbers, mean)

    # 输出平均数
    print("平均数为:", mean)
    # 输出中位数
    print("中位数为:", median)
    # 输出众数
    if len(modes) == 1:
        print("众数为:", modes[0])
    else:
        print("众数为:", ', '.join(str(mode) for mode in modes))
    # 输出方差
    print("方差为:", variance)

# 程序入口
if __name__ == '__main__':
    print("欢迎使用 Statistics Killer v0.1!")

    while True:
        # 调用主程序
        main()

        print("分析完毕，按任意键输入下一组数，按Esc键退出程序...")

        # 等待用户按下任意键
        key_pressed = msvcrt.getch()
        # 检查是否按下了 Esc 键，否则继续下一次循环
        if key_pressed == b'\x1b':
            break