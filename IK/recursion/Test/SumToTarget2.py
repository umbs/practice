def sum_to_target(n, target):
    def helper(n, start, running, target):
        if running == target:
            return True

        if start == len(n):
            return False

        select = helper(n, start+1, running+n[start], target)
        no_select = helper(n, start+1, running, target)

        return select or no_select

    return helper(n, 0, 0, target)


if __name__ == "__main__":
    print(sum_to_target([2, 5, 7], 6))
