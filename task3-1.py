
"""Создать класс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
Функции-члены реализуют запись и считывание полей (проверка корректности). Создать список объектов.
Вывести: a) список книг заданного автора; b) список книг, выпущенных после заданного года."""

class Book:
    __count = 0
    def __init__(self,id,Name,Author,Izd,Year,Count,Cost,Type):
        Book.__count += 1
        self.id = id
        self.Name = Name
        self.Author = Author
        self.Izdatel = Izd
        self.Year = Year
        self.Count = Count
        self.Cost = Cost
        self.Type = Type
    def __del__(self):
        Book.__count -= 1
    def __str__(self):
        return str(self.id)+" "+self.Name+" "+self.Author
    def author_books(self, name_author):
        if self.Author == name_author:
            return self.Name
    def year_books(self, year):
        if self.Year > year:
            return self.Name

library = [Book(1,'Onegin','Pushkin','NewLife',1980,45,678,'soft'),
         Book(2,'NewYear','Ivanov','NewLife',1970,45,678,'soft'),
         Book(3,'Dom','Kuprin','NewLife',1990,45,678,'soft'),
         Book(4,'ZooDom','Vernik','NewLife',1999,45,678,'soft'),
         Book(5,'Kapitan','Pushkin','NewLife',1950,45,678,'soft')]

#выводим все книги
print ("Список книг всех книг")
for i in library:
    print(i)

#выводим книги определенного автора
aut = "Pushkin"
print ("Список книг {}".format(aut))

for i in library:
    if print(i.author_books(aut)) is not None:
        print(i.author_books(aut))

#выводим книги после определенного года
year = 1980
print ("Список книг после {} года".format(year))
for i in library:
    if print(i.year_books(year)) is not None:
        print(i.year_books(year))



