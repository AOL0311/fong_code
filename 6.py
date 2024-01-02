def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        # 開始從3開始，只檢查奇數
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

time = 10
while time>0:
    number = int(input("請輸入一個數字："))

    if is_prime(number):
        print(f"{number} 是質數")
    else:
        print(f"{number} 不是質數")

    time -= 1