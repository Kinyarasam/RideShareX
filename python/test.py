#!/usr/bin/env python3

from models.user import User


email = 'test@test.com'
password = 'test Clear PWD'
f_name = "Test"
l_name = ""

user = User(email=email, password=password,
            first_name=f_name, last_name=l_name)
print(user)
user.save()
