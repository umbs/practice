def util(arr, k, start, sum_so_far, num_elems):
    if start == len(arr):
        if num_elems == 0 or sum_so_far != k:
            return False

        if sum_so_far == k:
            return True

    return util(arr, k, start+1, sum_so_far+arr[start], num_elems+1) or util(arr, k, start+1, sum_so_far, num_elems)


def check_if_sum_possible(arr, k):
    return util(arr, k, 0, 0, 0)


if __name__ == "__main__":
    # print(check_if_sum_possible([-5, -10], -15))
    print(check_if_sum_possible([1], 0))
