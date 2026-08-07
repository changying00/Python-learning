class FirstClass:
    def setdata(self,value):
        self.data = value

    def display(self):
        print(self.data)


if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()
    #
    x.setdata("coding")
    y.setdata(3.1415926)

    x.display()
    y.display()
    x.data  = "dgx"

    x.display()