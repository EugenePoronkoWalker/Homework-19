# Task 1
class Car:

    def __init__(self, model, year_of_manufacture, manufacturer, capacity, color, price):
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.price = price

    def change_model(self, model):
        self.model = model

    def change_year_of_manufacture(self, year_of_manufacture):
        self.year_of_manufacture = year_of_manufacture

    def change_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def change_capacity(self, capacity):
        self.capacity = capacity

    def change_color(self, color):
        self.color = color

    def change_price(self, price):
        self.price = price

    def show_model(self):
        return self.model

    def show_year_of_manufacture(self):
        return self.year_of_manufacture

    def show_manufacturer(self):
        return self.manufacturer

    def show_capacity(self):
        return self.capacity

    def show_color(self):
        return self.color

    def show_price(self):
        return self.price

    def show_all_car_info(self):
        print(f'Model name: {self.model} \n'
              f'Year of manufacture: {self.year_of_manufacture} \n'
              f'Manufacturer: {self.manufacturer} \n'
              f'Capacity: {self.capacity} \n'
              f'Color of car: {self.color} \n'
              f'Price: {self.price}')


my_car = Car('Audi', 1993, 'Germany', 1984, 'Red', 60000)
my_car.show_all_car_info()


# Task 2
class Book():

    def __init__(self, name, year_of_release, publisher, genre, author, price):
        self.name = name
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def change_name(self, new_name):
        self.name = new_name

    def change_year_of_release(self, new_year_of_release):
        self.year_of_release = new_year_of_release

    def change_publisher(self, new_publisher):
        self.publisher = new_publisher

    def change_genre(self, new_genre):
        self.genre = new_genre

    def change_author(self, new_author):
        self.author = new_author

    def change_price(self, new_price):
        self.price = new_price

    def show_name(self):
        return self.name

    def show_year_of_release(self):
        return self.year_of_release

    def show_publisher(self):
        return self.publisher

    def show_genre(self):
        return self.genre

    def show_author(self):
        return self.author

    def show_price(self):
        return self.price

    def show_all_book_info(self):
        print(f'Name: {self.name}\n'
              f'Year of release: {self.year_of_release}\n'
              f'Publisher: {self.publisher}\n'
              f'Genre: {self.genre}\n'
              f'Author: {self.author}\n'
              f'Price: {self.price}')


my_book = Book('Legend', 2007, 1954, 'Horror', 'Matheson', 500)
my_book.show_all_book_info()

# Task 3
class Stadium():

    def __init__(self, name, date_of_open, country, city, amount_of_people):
        self.name = name
        self.date_of_open = date_of_open
        self.country = country
        self.city = city
        self.amount_of_people = amount_of_people

    def change_name(self, new_name):
        self.name = new_name

    def change_date_of_open(self, new_date_of_open):
        self.date_of_open = new_date_of_open

    def change_country(self, new_country):
        self.country = new_country

    def change_city(self, new_city):
        self.city = new_city

    def change_amount_of_people(self, new_amount_of_people):
        self.amount_of_people = new_amount_of_people

    def show_name(self):
        return self.name

    def show_date_of_open(self):
        return self.date_of_open

    def show_country(self):
        return self.country

    def show_city(self):
        return self.city

    def show_amount_of_people(self):
        return self.amount_of_people

    def show_all_stadium_info(self):
        print(f'Name of stadium: {self.name}\n'
              f'Opening date: {self.date_of_open}\n'
              f'Country: {self.country}\n'
              f'City: {self.city}\n'
              f'Amount of people: {self.amount_of_people}')

first_stadium = Stadium('Kharkiv', '23 January', 'Ukraine', 'Kharkiv', 45000)
first_stadium.show_all_stadium_info()
