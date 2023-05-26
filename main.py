# 计算平均数
def calculateMean(numbers):
    # 计算平均值
    mean = sum(numbers) / len(numbers)

    # 返回计算结果
    return mean

# 计算中位数
def calculateMedian(numbers):
    # 对列表进行排序
    sortedNumbers = sorted(numbers)
    
    # 获取列表长度
    length = len(sortedNumbers)
    
    # 判断列表长度的奇偶性
    if (length % 2 == 0):
        # 对于偶数长度的列表，中位数为中间两个数的平均值
        midIndex1 = length // 2
        midIndex2 = midIndex1 - 1  # 之所以是减一不是加一是因为列表索引是从0开始，因此 length // 2 刚好是 后一个数，减去一刚好是前一个数
        median = (sortedNumbers[midIndex1] + sortedNumbers[midIndex2]) / 2
    else:
        # 对于奇数长度的列表，中位数为中间的数
        midIndex = length // 2
        median = sortedNumbers[midIndex]
    
    return median

# 计算方差
def calculateVariance(numbers, mean):
    
    # 计算每个数与平均值的差的平方
    squaredDiff = [(x - mean) ** 2 for x in numbers]
    
    # 计算差的平方的平均值
    variance = sum(squaredDiff) / len(numbers)
    
    # 返回计算结果
    return variance

def main():
    # 获取输入的一组数
    inputNumbers = input("请输入一组数（以空格分隔）：").split()

    # 转换为数字列表
    numbers = [float(x) for x in numbers]

    # 计算平均数
    mean = calculateMean(inputNumbers)

    # 计算中位数
    median = calculateMedian(inputNumbers)

    # 计算方差
    variance = calculateVariance(inputNumbers, mean)

    # 输出结果
    print("方差为:", variance)

if __name__ == '__main__':
    main()