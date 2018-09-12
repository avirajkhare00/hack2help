from django.contrib.auth.models import User
from front_end.models import UserInfo

class signUpLayer:

    def __init__(self, first_name, last_name, email, password, dob, disease,city, address, pin_code):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.disease = disease
        self.city = city
        self.address = address
        self.email = email
        self.password = password
        self.pin_code = pin_code

    def signup_user(self):

        new_user = User()

        new_user.username = self.email.split('@')[0]
        new_user.email = self.email
        new_user.first_name = self.first_name
        new_user.last_name = self.last_name
        new_user.set_password(self.password)
        new_user.save()

    def new_user_create_id(self):

        new_user = UserInfo()

        new_user.email = User.objects.get(email=self.email)
        #new_user.username = User.objects.get(email=self.username)
        new_user.age = self.dob
        new_user.disease = self.disease
        new_user.city = self.city
        new_user.address = self.address
        new_user.pin_code = self.pin_code
        new_user.save()
