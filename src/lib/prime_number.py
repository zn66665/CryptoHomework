import random

def is_prime(num, k=5):
    """Miller-Rabin素性测试"""
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False

    # 将 num - 1 表示为 2^r * d 的形式
    r, d = 0, num - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # 进行 k 次测试
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits=1024):
    """生成一个指定位数的大素数"""
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1  # 设置最高位和最低位为1确保足够位数且奇数
        if is_prime(candidate):
            return candidate
