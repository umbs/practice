class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):
    def serialize(self, root):
        def util(node):
            if not node:
                ser.append("*")
                return

            ser.append(node.val)
            util(node.left)
            util(node.right)

        ser = list()
        util(root)

        return ''.join(ser)

    def deserialize(self, stream):
        def util():
            val = next(obj)
            if val == '*':
                return None
            node = Node(val)
            node.left = util()
            node.right = util()

            return node

        obj = iter(stream.split())
        return util()
