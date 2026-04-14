from Sorting.util import file_to_list

def radix_sort(random_list: list = file_to_list()):
    bucket_list_unit = [[] for _ in range(10)] # 0 até 9
    bucket_list_decimal = [[] for _ in range(10)] # 0X até 9X
    output_list = []

    for number in random_list:
        if 1 <= number < 10:
            i = number
        else:
            i = (number % 10)
        bucket_list_unit[i].append(number)

    for bucket in bucket_list_unit:
        #print(bucket)
        for number in bucket:
            if 1 <= number < 10:
                i = 0
            else:
                i = number // 10
            bucket_list_decimal[i].append(number)

    for bucket in bucket_list_decimal:
        for number in bucket:
            output_list.append(number)

    #print(output_list)
    return output_list