def merge_sorting(lst):
    inversion_count = 0
    if len(lst) > 1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]

        inversion_count += merge_sorting(left_lst)
        inversion_count += merge_sorting(right_lst)

        i = j = k = 0

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
                inversion_count += (len(left_lst) - i)
            k += 1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1

    return inversion_count