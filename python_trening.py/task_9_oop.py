# #new*
# class Button:
#     type: str = 'Кнопка'
#
#    # new*
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# home = Button("Домой", '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' +home.link)
#
# print('\n')
#
# print(catalog_msk)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' +catalog_msk.link)



# class ButtonTwo:
#     def __init__(self, text, link, lok):
#         self.text = text
#         self.link = link
#         self.lok = lok
#
#     def click(self):
# #         return "Клик по локатору - {}".format(self.lok)
# home_two = ButtonTwo('Домой', '/home', 'button#home')
#
# print(home_two.click())

class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text=text

search = Input('input#search', 'текст ')
print(search.text)


class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text=text

Button1 = Input('input#button1', 'текст ')
print(Button1.loc)


class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text=text

Title1 = Input('input#Title1', 'текст ')
print(Title1.loc)

class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text=text

Link1 = Input('input#Link1', 'текст ')
print(Link1.loc)




