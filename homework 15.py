# Task 1
class Person():
    name = 'Ivan'
    surname = 'Petrov'
    middle_name = 'Vladimirovich'
    date_of_birth = '01.12.1990'
    contact_number = '380933033330'
    town = 'Kiev'
    country = 'Ukraine'
    street = 'Matrosova'
    house = 22

    def show_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

    def show_surname(self):
        return self.surname

    def change_surname(self, new_surname):
        self.surname = new_surname

    def show_middle_name(self):
        return self.middle_name

    def change_middle_name(self, new_middle_name):
        self.middle_name = new_middle_name

    def show_date_of_birth(self):
        return self.date_of_birth

    def change_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def show_contact_number(self):
        return self.contact_number

    def change_contact_number(self, new_contact_number):
        self.contact_number = new_contact_number

    def show_town(self):
        return self.town

    def change_town(self, new_town):
        self.town = new_town

    def show_country(self):
        return self.country

    def change_country(self, new_country):
        self.country = new_country

    def show_street(self):
        return self.street

    def change_street(self, new_street):
        self.street = new_street

    def show_house(self):
        return self.house

    def change_house(self, new_house):
        self.house = new_house

    def show_all_data(self):
        return self.name, self.surname, self.middle_name, self.date_of_birth, \
               self.contact_number, self.town, self.country, self.street, self.house


first_person = Person()
print(first_person.show_all_data())


# Task 2

class Town():
    name_of_town = 'Mena'
    name_of_region = 'Chernigov'
    name_of_country = 'Ukraine'
    number_of_residents = 2000000
    index = 10001

    def show_name_of_town(self):
        return self.name_of_town

    def change_name_of_town(self, new_name_of_town):
        self.name_of_town = new_name_of_town

    def show_name_of_region(self):
        return self.name_of_region

    def change_name_of_region(self, new_name_of_region):
        self.name_of_region = new_name_of_region

    def show_name_of_country(self):
        return self.name_of_country

    def change_name_of_country(self, new_name_of_country):
        self.name_of_country = new_name_of_country

    def show_number_of_residents(self):
        return self.number_of_residents

    def change_number_of_residents(self, new_number_of_residents):
        self.number_of_residents = new_number_of_residents

    def show_index(self):
        return self.index

    def change_index(self, new_index):
        self.index = new_index

    def show_all_data(self):
        return self.name_of_town, self.name_of_region, self.name_of_country, \
               self.number_of_residents, self.index


fist_town = Town()
print(fist_town.show_all_data())


# Task 3

class Country():
    name_of_country = 'Ukraine'
    name_of_continent = 'Europe'
    number_of_residents = 40000000
    phone_code = '+380'
    name_of_first_city = 'Kiev'
    name_of_second_city = 'Chernigov'
    name_of_third_city = 'Poltava'

    def show_name_of_coutnry(self):
        return self.name_of_country

    def change_name_of_country(self, new_name_of_country):
        self.name_of_country = new_name_of_country

    def show_name_of_continent(self):
        return self.name_of_continent

    def change_name_of_continent(self, new_name_of_continent):
        self.name_of_continent = new_name_of_continent

    def show_number_of_residents(self):
        return self.number_of_residents

    def change_number_of_residents(self, new_number_of_residents):
        self.number_of_residents = new_number_of_residents

    def show_phone_code(self):
        return self.phone_code

    def change_phone_code(self, new_phone_code):
        self.phone_code = new_phone_code

    def show_name_of_first_city(self):
        return self.name_of_first_city

    def change_name_of_first_city(self, new_name_of_first_city):
        self.name_of_first_city = new_name_of_first_city

    def show_name_of_second_city(self):
        return self.name_of_second_city

    def change_name_of_second_city(self, new_name_of_second_city):
        self.name_of_second_city = new_name_of_second_city

    def show_name_of_third_city(self):
        return self.name_of_third_city

    def change_name_of_third_city(self, new_name_of_third_city):
        self.name_of_third_city = new_name_of_third_city

    def show_all_data(self):
        return self.name_of_country, self.name_of_continent, self.number_of_residents, self.phone_code, \
               self.name_of_first_city, self.name_of_second_city, self.name_of_third_city


my_country = Country()
print(my_country.show_all_data())


# Task 4

class Fraction():
    numerator = 1
    denominator = 2

    def show_numerator(self):
        return self.numerator

    def change_numerator(self, new_numerator):
        self.numerator = new_numerator

    def show_denominator(self):
        return self.denominator

    def change_denominator(self, new_denominator):
        self.denominator = new_denominator

    def change_numerator_and_denominator(self, new_numerator, new_denominator):
        self.numerator = new_numerator
        self.denominator = new_denominator

    def action_multiplication(self):
        return self.numerator * self.denominator

    def action_addition(self):
        return self.numerator + self.denominator

    def action_subtraction(self):
        return self.numerator - self.denominator

    def action_division(self):
        return self.numerator / self.denominator

my_own_actions = Fraction()



