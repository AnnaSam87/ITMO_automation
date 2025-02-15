class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh

    def square(self):
        print(self.width*self.heigh)

    def perimetr(self):
        print(2*(self.width + self.heigh))

Rectangle1 = Rectangle(3,4)
Rectangle2 = Rectangle (10,20)
Rectangle3 = Rectangle (1,1)
Rectangle1.square(), Rectangle1.perimetr()
Rectangle2.square(), Rectangle2.perimetr()
Rectangle3.square(), Rectangle3.perimetr()


class Math:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def addition(self):
        print(f'Сумма чисел составляет {self.a+self.b}')

    def multiplication(self):
        print(f'Произведение чисел составляет {self.a * self.b}')

    def division(self):
        print(f'Частное от деления первого числа на второе составляет {self.a / self.b}')

    def substraction(self):
        print(f'Разница между первым и вторым числом составляет {self.a - self.b}')

Math1=Math(8,2)
Math1.addition()
Math1.multiplication()
Math1.division()
Math1.substraction()


class Button:
    def __init__(self, type, text, lok=None):
        self.type=type
        self.text=text
        self.lok=lok

    def press_button(self):
        print(f'Клик по кнопке {self.text}')

Text_Box = Button ('Кнопка', 'Text Box')
print(Text_Box.text)
Check_Box = Button ('Кнопка', 'Check Box')
print(Check_Box.text)
Radio_Button = Button ('Кнопка', 'Radio Button')
print(Radio_Button.text)
Buttons = Button ('Кнопка', 'Buttons')
print(Buttons.text)
Links = Button ('Кнопка', 'Links')
print(Links.text)
Broken_Links_Images = Button ('Кнопка', 'Broken Links - Images')
print(Broken_Links_Images.text)
Upload_and_Download = Button ('Кнопка', 'Upload and Download')
print(Upload_and_Download.text)
Dynamic_Properties = Button ('Кнопка', 'Dynamic Properties')
print(Dynamic_Properties.text)

Text_Box.press_button()
Check_Box.press_button()
Radio_Button.press_button()
Buttons.press_button()
Broken_Links_Images.press_button()
Upload_and_Download.press_button()
Dynamic_Properties.press_button()
