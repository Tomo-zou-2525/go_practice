# input_list = [int(input()) for i in range(4)]
# input_list = [5,3,10000,1000]

# lodging_day = input_list[0]
# basic_charge_day = input_list[1]

# basic_charge = input_list[2]
# consective_charge = input_list[3]


lodging_day = int(input())
basic_charge_day = int(input())
basic_charge = int(input())
consective_charge = int(input())

if lodging_day < basic_charge_day:
    total_ammount = lodging_day * basic_charge_day
    print(total_ammount)
else:
    total_ammount = (basic_charge_day * basic_charge) + (lodging_day - basic_charge_day) * consective_charge

print(total_ammount)
