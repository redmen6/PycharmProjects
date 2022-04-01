def sum_list_1(dataset: list):
    res_for_return = 0
    for number_of_list in my_list:
        num_sum = number_of_list
        num_num = 0
        while num_sum != 0:
            num_num += num_sum % 10
            num_sum //= 10

        if num_num % 7 == 0:
            res_for_return += number_of_list

    return res_for_return


my_list = []
for idx in range(0, 1000, 2):
    my_list.append((idx + 1) ** 3)

result_1 = sum_list_1(my_list)
print(result_1)

for idx in range(len(my_list)):
    my_list[idx] += 17

result_2 = sum_list_1(my_list)
print(result_2)

