from faker import Faker
class Randomdata:
    def __init__(self):
        self.faker = Faker()
#generate random data for the application

    def generate_random_username(self):
        return self.faker.user_name()

    def generate_random_password(self):
        return self.faker.password()

    def generate_random_first_name(self):
        return self.faker.first_name()

    def generate_random_last_name(self):
        return self.faker.last_name()

    def generate_random_postal_code(self):
        return self.faker.postcode()

    def generate_random_email(self):
        return self.faker.email()

    def generate_random_password(self):
        return self.faker.password()

    def generate_random_name(self):
        return self.faker.name()

    def generate_random_phone_number(self):
        return self.faker.numerify("##########")
        
    def generate_random_event_title(self):
        return self.faker.sentence(nb_words=4, variable_nb_words=True)