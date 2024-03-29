#!/usr/bin/env python3

import base64
# from utils.redis_client import RedisClient
from models.user import User
from models.ride import Ride
from models.ride_request import RideRequest


email = 'test@test.com'
password = 'test Clear PWD'
f_name = "Test"
l_name = ""

user = User(email=email, password=password,
            first_name=f_name, last_name=l_name)
print(user.to_dict())
user.save()

capacity = 2
plate_no = "K** 2**F"

ride = Ride(plate_no=plate_no, capacity=capacity)
print("\n-----\n")
print(ride.to_dict())
ride.save()

origin="nairobi"
dest="CBD"
ride_request = RideRequest(ride_id=ride.id, user_id=user.id,
                           origin=origin, destination=dest)
print("\n-----\n")
print(ride_request.to_dict())
ride_request.save()


# r = RedisClient()
# print(r.isAlive())

print("\n-----\n")
print(User.find(email=email, password=password))

auth_str = '{}:{}'.format(email, password)
encoded_str = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
print("\n-----\n")
print(encoded_str)   # dGVzdEB0ZXN0LmNvbTp0ZXN0IENsZWFyIFBXRA==