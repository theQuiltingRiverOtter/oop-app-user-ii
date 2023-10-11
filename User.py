# your User class goes here
class User:
    all_users = {}
    all_user_posts = {}

    @classmethod
    def view_all_users(cls):
        for user in cls.all_users.values():
            print(user)

    @classmethod
    def view_all_user_posts(cls):
        for user, posts in cls.all_user_posts.items():
            if len(posts) > 0:
                print(f"**{user.title()}**")
                print("---------")
                for post in posts:
                    print(post)
                print()

    def __init__(
        self, name: str, age: int, email: str = None, phone_number: str = None
    ):
        # Add validation for values
        self.__name = name
        self.__age = age
        self.__email = email
        self.__phone_number = phone_number
        self._user_posts = []
        User.all_users[self.name] = self
        User.all_user_posts[self.name] = self._user_posts

    def __str__(self):
        if self.__email and self.__phone_number:
            return f"{self.__name} -  Age: {self.__age}, Email: {self.__email}, Phone Number: {self.__phone_number}"
        else:
            return f"{self.__name} - Age: {self.__age}"

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email

    @property
    def phone_number(self):
        return self.__phone_number

    @name.setter
    def name(self, name: str):
        # validation for name? should it be two names?
        if len(name) < 2:
            raise ValueError("Name must be at least two characters long")
        if type(name) != str:
            raise TypeError("Name must be of type str")
        else:
            self.__name = name

    @age.setter
    def age(self, age: int):
        if type(age) != int:
            raise TypeError("Age must be of type int")
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")
        else:
            self.__age = age

    @email.setter
    def email(self, email: str):
        # use regex to validate email
        if "@" not in email:
            raise ValueError("email must include an @ symbole")
        else:
            self.__email = email

    @phone_number.setter
    def phone_number(self, phone_number: str):
        # use regex to validate phone_number
        numbers = "0123456789"
        phone_nums = ""
        for num in phone_number:
            if num in numbers:
                phone_nums += num
        if len(phone_nums) != 10:
            raise ValueError("Phone number should be 10 digits long")
        else:
            self.__phone_number = phone_number

    def add_post(self, post):
        self._user_posts.append(post)
        User.all_user_posts[self.name] = self._user_posts

    def delete_post(self, post_to_delete):
        index = None
        for i, post in enumerate(self._user_posts):
            if post == post_to_delete:
                index = i
        if index != None:
            self._user_posts.splice(index, 1)
        User.all_user_posts[self.name] = self._user_posts

    def view_posts(self):
        for post in self._user_posts:
            print(post)


megan = User("Megan", 38, "thequiltingriverotter@gmail.com", "123-456-7890")
john = User("John", 25, "fakeemail@gmail.com", "978-456-1231")
bob = User("Bob", 50)

megan.add_post("This is a great app")
john.add_post("Hi")
megan.add_post("Code Platoon is the best bootcamp")
megan.view_posts()

User.view_all_users()
print()
User.view_all_user_posts()
