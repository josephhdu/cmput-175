import random

class Card:

    def __init__(self, colours, depth):
        self.colours = colours
        self.depth = depth
        self.length = colours
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
        alphabet = alphabet[0: colours]
        self.__beads = []
        for i in range(self.length):
            for j in range(self.depth):
                self.__beads.append(alphabet[i])
        random.shuffle(self.__beads)

    def reset(self):
        random.shuffle(self.__beads)
        return self.__beads

    def show(self):
        print(self.__beads)
        for i in range(self.depth):
            print("|", end="")
            for j in range(self.length):
                if j > 0:
                    print("", end=" ")
                print(self.__beads[self.depth * j + i], end="")
            print("|")

    def basicStr(self):
        bString = "".join(self.__beads)
        return bString

    def abacoShow(self):
        #change a bit
        abaco = []
        for i in range(self.depth):
            pass

    def fuck(self):
        show_list = []
        for i in range(self.depth):
            str_row = ''
            str_row += '|'
            for colour in range(self.colours):
                if colour > 0:
                    str_row += ' '
                str_row += self.__beads[self.depth * colour + i]
            str_row += '|'
            show_list.append(str_row)
        return show_list


    # def nested(self):
    #     nList = []
    #     # for i in range(self.length):
    #     for i in range(self.length):
    #         nList.append(self.stack(i+1))
    #     print(nList)

    def stack(self, number):
        if number > self.length:
            raise Exception("Stack does not exist")
        start = number * self.depth - self.depth
        end = start + self.depth
        return self.__beads[start:end]

    def __str__(self,):
        i = self.depth
        info = self.__beads.copy()
        while i < len(info):
            info.insert(i,"||")
            i += self.depth + 1
        info.insert(0, "|")
        info.append("|")
        aString = "".join(info)
        return aString
            

    def replace(self, filename,n):
        file = open(filename,"r")
        data = file.readlines()
        return data[n-1]


if __name__ == '__main__':
    c = Card(3,3)
    c.show()
    print(c.stack(2))
    print(c.__str__())
    print(c.replace("replace.txt", 3))
    print(c.basicStr())
    print(c.fuck())