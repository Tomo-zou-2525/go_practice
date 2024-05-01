def calculate_accommodation_cost(N, K, X, Y):
    basic_cost = min(N, K) * X
    consecutive_cost = max(0, N - K) * Y
    total_cost = basic_cost + consecutive_cost
    return total_cost

# 入力を受け取る
N = int(input("宿泊日数を入力してください: "))
K = int(input("基本宿泊日数を入力してください: "))
X = int(input("基本宿泊費を入力してください: "))
Y = int(input("追加宿泊費を入力してください: "))

# 宿泊費を計算
total_ammount = calculate_accommodation_cost(N, K, X, Y)
print("宿泊費用は{}円です。".format(total_ammount))
