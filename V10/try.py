import math
import time
import random

from sklearn.utils import assert_all_finite


class Operater:
    def __init__(self):
        pass


class Plus(Operater):
    def __init__(self):
        pass
        super()


class stutures_single:
    def __init__(self, data):
        self.parent = None
        if self.checkSytax(data) == False:
            raise Exception(f"Sorry, {data} is not a stutures_single")
        elif type(data) == stutures_single:
            raise Exception(
                f"Sorry, {data} type(data) is not a stutures_single")

        else:
            try:
                tem = int(data)
                self.type = 'number'
                self.data = tem
            except ValueError as e:
                self.type = 'variable'
                self.data = data

    def checkSytax(self, data):
        is_number = False
        is_variable = False
        for i in str(data):
            a = i.isdigit()
            b = i.isalpha()
            if a:
                is_number = True
            if b:
                is_variable = True
            if a == False and b == False and i != ".":
                return False

        return is_number != is_variable

    def __str__(self):
        return str(self.data)

    def simplify(self): return

    def __restructure(self, other, tem):
        tem.parent = self.parent or other.parent or None
        self.parent = tem
        other.parent = tem
        self.simplify()
        other.simplify()
        return tem

    def __add__(self, other):
        if type(other) == int:
            other = stutures_single(str(other))
        tem = stutures(self, other, "+")
        self.__restructure(other, tem)
        return tem

    def __sub__(self, other):
        if type(other) == int:
            other = stutures_single(str(other))
        tem = stutures(self, other, "-")
        self.__restructure(other, tem)
        return tem

    def __mul__(self, other):
        if type(other) == int:
            other = stutures_single(str(other))
        tem = stutures(self, other, "*")
        self.__restructure(other, tem)
        return tem

    def __truediv__(self, other):
        if type(other) == int:
            other = stutures_single(str(other))
        tem = stutures(self, other, "/")
        self.__restructure(other, tem)
        return tem

    def __eq__(self, other):
        return str(self) == str(other)


class stutures(stutures_single):
    def __init__(self, childrenLeft, childrenRight, operater, parent=None):
        self.childrenLeft = childrenLeft
        self.childrenRight = childrenRight
        self.parent = parent
        self.operater = operater
        self.simplify()

        self.data = None
        self.tpye = None
        self.checkSytax = None

    def simplify(self):
        # print("Simplifying")
        # Trivial caclulation
        if type(self.childrenLeft) == type(self.childrenRight) == stutures_single:
            if self.childrenLeft.type == self.childrenRight.type == "number":
                tem = 0

                if self.operater == "+":
                    tem = self.childrenLeft.data + self.childrenRight.data
                elif self.operater == "-":
                    tem = self.childrenLeft.data - self.childrenRight.data
                elif self.operater == "*":
                    tem = self.childrenLeft.data * self.childrenRight.data
                elif self.operater == "/":
                    tem = self.childrenLeft.data / self.childrenRight.data

                if self.parent is not None:
                    if self.parent.childrenLeft == self:
                        self.parent.childrenLeft = stutures_single(str(tem))
                    elif self.parent.childrenRight == self:
                        self.parent.childrenRight = stutures_single(str(tem))
                        self.simplify()
        # Similar term
        if self.childrenLeft == self.childrenRight:
            if self.operater == "+":
                self.childrenLeft = stutures_single("2")
                self.operater = "*"
                self.childrenRight = self.childrenRight
                self.simplify()
            elif self.operater == "*":
                pass

        # Number first
        if type(self.childrenRight) == stutures_single and type(self.childrenLeft) != stutures_single:
            if self.childrenRight.type == "number":
                tem = self.childrenLeft
                self.childrenLeft = self.childrenRight
                self.childrenRight = tem
                self.simplify()

    def __str__(self):
        return f"({self.childrenLeft}{self.operater}{self.childrenRight})"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        elif type(self) == type(other) == stutures:
            return self.childrenLeft == other.childrenLeft and self.childrenRight == other.childrenRight and self.operater == other.operater
        elif type(self) == type(other) == stutures_single:
            return self == other

# TODO: operater ^


memory = dict()


def _construct_tree(expession: str):
    def construct_single(expession: str):
        # if expession in memory:
        #     print("expession in memory: ", expession,
        #           memory[expession][1:len(expession)-1])
        #     # return stutures_single(memory[expession][1:len(memory[expession])-1])
        return stutures_single(expession)

    def construct_with_mutimpl(expession: str):
        childrenLeft_poiter = 0

        if "*" in expession or "/" in expession:
            while childrenLeft_poiter < len(expession) and expession[childrenLeft_poiter] not in ["*", "/"]:
                childrenLeft_poiter += 1
            tem = expession[0:childrenLeft_poiter]
            tem = stutures_single(tem)
            childrenLeft = tem
            childrenRight = _construct_tree(
                expession[childrenLeft_poiter+1:len(expession)])
            operater = expession[childrenLeft_poiter]
            root = stutures(childrenLeft, childrenRight, operater)
            childrenLeft.parent = root
            childrenRight = root
            return root
        else:
            tem = expession

            return construct_single(tem)

    childrenLeft_poiter = 0
    if "+" in expession or "-" in expession:
        while childrenLeft_poiter < len(expession) and expession[childrenLeft_poiter] not in ["+", "-"]:
            childrenLeft_poiter += 1

        tem = expession[0:childrenLeft_poiter]
        tem = construct_with_mutimpl(tem)
        childrenLeft = tem
        childrenRight = _construct_tree(
            expession[childrenLeft_poiter+1:len(expession)])
        operater = expession[childrenLeft_poiter]
        root = stutures(childrenLeft, childrenRight, operater)
        childrenLeft.parent = root
        childrenRight = root
        return root
    else:
        tem = expession
        return construct_with_mutimpl(tem)


def construct_tree(expession: str):
    # construct_tree with ()
    global memory

    def randStr(N=32):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        import random
        return ''.join(random.choice(chars) for _ in range(N))

    def sub_expession(expession: str):
        expession = expession
        sub_expession = ""
        key = randStr()

        tem = expession
        first = 0
        last = len(tem)

        while "(" in tem[first:last] or ")" in tem[first:last]:
            if ")" in tem[first:last]:
                last -= 1
            else:
                first += 1

        if first == 0 and last == len(expession):
            pass
        else:
            first -= 1
            last += 1

        expession = expession[0:first]+key+expession[last:len(expession)]
        return expession, tem[first:last], key
    # memory = dict()
    tem = expession
    while "(" in tem or ")" in tem:
        e, s, k = sub_expession(tem)
        memory[k] = s[1:len(s)-1]
        tem = e
    # return memory, tem
    root = _construct_tree(tem)
    for x in memory.keys():
        memory[x] = _construct_tree(memory[x])
    root = assert_all_node(root)
    root = assert_all_node(root)

    return root


def assert_all_node(root):
    print("root", root)
    if type(root) == stutures_single:
        if root.data in memory:
            print("root.data in memory", root.data, memory)
            if root.parent and root.parent.childrenLeft == root:
                root.parent.childrenLeft = memory[root.data]
                memory[root.data].parent = root.parent
            elif root.parent and root.parent.childrenRight == root:
                root.parent.childrenRight = memory[root.data]
                memory[root.data].parent = root.parent
            else:
                root = memory[root.data]
    else:
        childrenLeft = root.childrenLeft
        childrenRight = root.childrenRight
        assert_all_node(childrenLeft)
        assert_all_node(childrenRight)

    return root

# print(construct_tree("123(45)6"))
# print(construct_tree("123456"))
# print(construct_tree("(12(34)56)"))
# print(construct_tree("(12(3(4)5)6)"))

# print(construct_tree("0+1"))
# print(construct_tree("12+3+4"))
# print(construct_tree("12+3+4+5+6+3"))
# print(construct_tree("1*2/3"))


print(construct_tree("4*(456+6)"))
print(memory)


def main():
    x = stutures_single("x")
    y = stutures_single("y")
    z = stutures_single("2")
    a = (x+y)*(x+y)
    print(a)
    b = x*x + z*x*y + y*y
    print(b)


if __name__ == '__main__':
    pass
    # main()
