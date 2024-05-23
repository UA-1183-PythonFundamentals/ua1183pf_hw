class User:
    def __init__(self, user_id, name, email, age, country):
        self.user_id = int(user_id)
        self.name = name
        self.email = email
        # self.age = age
        self.__age = int(age)
        self.country = country

    def __repr__(self):
        return (f"User(user_id={self.user_id}, name='{self.name}', email='{self.email}', "
                f"age={self.age}, country='{self.country}')")
    def get_csv_format(self):
        return f"{self.user_id},{self.name},{self.email},{self.age},{self.country}\n"
    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            # self.__age = int(age)
            self.__age = age
    age = property(get_age, set_age)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "country": self.country
        }