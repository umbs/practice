class SubArrayProduct:
    """
    Assume all numbers > 0 and there's no integer overflow

    Reference:
        * https://www.geeksforgeeks.org/number-subarrays-product-less-k/
    """
    def nums_subarrays_product_k(self, arr, K):
        i, j = 0, 0

        ans = []
        nums = 0
        ln = len(arr)

        prod = 1
        while j < ln:
            while i < j and prod * arr[j] >= K:
                prod /= arr[i]
                i += 1
            if prod < K:
                prod *= arr[j]
                nums += 1 + (j-i)
                j += 1

        return nums, ans


if __name__ == "__main__":
    a = SubArrayProduct()
    # arr = [3, 2, 1, 4]
    # arr = [3, 2, 5, 6]
    arr = [3, 2, 1, 4, 5, 6]
    # arr = [4, 5, 6]
    K = 30
    count, ans = a.nums_subarrays_product_k(arr, K)
    print count, ans
