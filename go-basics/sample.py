# students = int(input())

# for i in range(students):
#     initial = 1
#     num = i * 1
#     result = initial + num
#     print(result)
# for i in range(1, 8,2):
#     print(i)
#     print("unko")

### output 1,3,5,7

# n = int(input())

# total_amount = 0

# for i in range(n + 1 ):
#     num = 0
#     num += 1 * i
#     total_amount += num

# print(total_amount)

# num = [int(input()) for i in range(4)]

# print(num)

# some_list = [1,2,3,4,5]
# i = 0

# atcode_input = [int(input()) for i in range(4)]
# atcode_input = [3, 5, 10000, 9000] A.30000
atcode_input = [5, 3, 10000, 9000] # A.49000

def accommodation_charge(atcode_input):
    lodging_day = atcode_input[0]
    print("lodging_day")
    print(lodging_day)
    basic_lodging_pay = atcode_input[1]
    days_for_which_consecutive = atcode_input[1] + 1
    print("days_for_which_consecutive")
    print(days_for_which_consecutive)

    basic_lodging_day_charge = atcode_input[2]
    print("basic_lodging_day_charge")
    print(basic_lodging_day_charge)
    consecutive_lodging_day_charge = atcode_input[3]
    print("consecutive_lodging_day_charge")
    print(consecutive_lodging_day_charge)

    consecutive_day = lodging_day - atcode_input[1]
    print("consecutive_day")
    print(consecutive_day)
    
    total_ammount_basic = basic_lodging_pay * basic_lodging_day_charge
    print("total_ammount_basic")
    print(total_ammount_basic)

    total_ammount_add = consecutive_day * consecutive_lodging_day_charge
    print("total_ammount_add")
    print(total_ammount_add)

    total_ammount = total_ammount_basic + total_ammount_add
    print(f"宿泊料金 + {total_ammount}")
    return  total_ammount

    # total_ammount_basic = lodging_day * basic_lodging_day_charge
    # total_ammount = total_ammount_basic
    # print(f"超過料金込み + {total_ammount}")
    # return  total_ammount
        
accommodation_charge(atcode_input)


# def accommodation_charge(num):
#     lodging_day = num[0] 
#     over_lodging_day = num[1] + 1
#     if lodging_day > over_lodging_day:
#         total_ammount = lodging_day * num[2]
#     elif lodging_day < over_lodging_day:
#         total_ammount
#     total_ammount = first_lodging_day * num[2]
#     print(total_ammount)
#     return total_ammount

# def accommodation_charge_first(num):
#     first_lodging_day = num[0] 
#     second_lodging_day = num[1] + 1
#     total_ammount = first_lodging_day * num[2]
#     print(total_ammount)
#     return total_ammount

# def accommodation_charge_second(num):
#     second_lodging_day = num[1] + 1
#     total_ammount = second_lodging_day * num[3]
#     print(total_ammount)
#     return total_ammount

# print("合計金額は")
# print(accommodation_charge_first(num) + accommodation_charge_second(num))