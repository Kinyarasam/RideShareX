#!/usr/bin/env python3

from models.user import User

email = 'test@test.com'
password = 'test Clear PWD'

user = User(email=email, password=password)
print(user)
