def transform_string(number: int) -> str:
    global res_for_return
    if n % 10 == 1:
        res_for_return = f'{n} процент'
    elif 1 < n % 10 < 5:
        res_for_return = f'{n} процента'
    elif 4 < n % 10 < 10 or n % 10 == 0:
        res_for_return = f'{n} процентов'

    return res_for_return


for n in range(1, 101):
    print(transform_string(n))