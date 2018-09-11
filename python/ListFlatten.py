class ListFlatten:
    def list_flatten(self, llist):
        res = []
        for l in llist:
            if hasattr(l, "__iter__")


if __name__ == "__main__":
    a = ListFlatten()
    # llist = [range(4), range(7)]
    llist = [1, [2, 3], [[[4]]]]
    print a.list_flatten(llist)
