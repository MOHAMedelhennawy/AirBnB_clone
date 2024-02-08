#!/usr/bin/python3
from models import storage
import json
import models
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()

print
print('===' * 50)
my_mode2 = my_model
print(type(my_mode2))