input_list = [int(input()) for i in range(4)]
# input_list = [5, 3, 10000, 9000] # 48000

def ammount_calc(input_list):

    lodging_day = input_list[0]
    basic_cahrge_day = input_list[1]
    consecutive_cahrge_line = input_list[1] + 1

    basic_charge = input_list[2]
    consective_charge = input_list[3]

    # 費用計算
    basic_ammount = basic_cahrge_day * basic_charge


    if lodging_day > basic_cahrge_day:
        # 超過費用が適用される日数を計算
        consective_day = lodging_day - basic_cahrge_day
        consective_ammount = consective_day * consective_charge
        # 基本費用を計算
        basic_ammount = basic_cahrge_day * basic_charge
        # 宿泊費用を計算
        total_ammount = basic_ammount + consective_ammount
        print("超過費用込み")
        print(total_ammount)
        return total_ammount
    else:
        # 宿泊費用を計算
        total_ammount = lodging_day * basic_charge
        print("基本費用のみ")
        print(total_ammount)
        return total_ammount


ammount_calc(input_list)