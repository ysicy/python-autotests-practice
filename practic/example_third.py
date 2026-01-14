import json
from xml.etree.ElementTree import indent

from faker import Faker
#
values =  {2, 1, 4, 9, 16, 25}
keys = {'a','b','c','d','e','w'}
result = dict(zip(keys, values))
wrapper = {"data": result}
new_wrapper = {"attribute": wrapper}
print(new_wrapper)
#
# my_json = json.dumps(new_wrapper, indent=4)
# print(my_json)
#
# load_str = json.loads(my_json)
# print(load_str)
#
# load_str["attribute"]["data"]["a"] = "hello"
# load_str["attribute"]["data"]["b"] = "world"
# load_str["attribute"]["data"]["c"] = "myjson"
# load_str["attribute"]["data"]["d"] = "epta"
# load_str["attribute"]["data"]["e"] = "opa"
# load_str["attribute"]["data"]["w"] = "horosho"
#
# data_dict = load_str["attribute"]["data"]
#
# add_new_attribute = {
#     "alpha": data_dict["a"],
#     "beta": data_dict["b"],
#     "gamma": data_dict["c"],
#     "delta": data_dict["d"],
#     "epsilon": data_dict["e"],
#     "zeta": data_dict["w"],
# }
#
# load_str["attribute"]["data"] = add_new_attribute
#
# my_new_json = json.dumps(load_str, indent=4)
# print(my_new_json)
# loadim_json_to_str = json.loads(my_new_json)
# print(loadim_json_to_str)
#
# assert "gamma" in loadim_json_to_str["attribute"]["data"]
# assert "delta" in loadim_json_to_str["attribute"]["data"]
# assert loadim_json_to_str["attribute"]["data"]["beta"] == "world"
# assert "data" in loadim_json_to_str["attribute"]
# assert "zeta" in loadim_json_to_str["attribute"]["data"]
# assert "epsilon" in loadim_json_to_str["attribute"]["data"]
#
#

faker = Faker()
Faker.seed(12345)
def generate_users(count=10):
    users = []
    for i in range(count):
        user = {
            "id": i + 1,
            "user": {
            "name": faker.name(),
            "email": faker.email(),
                "profile": {
                    "age": faker.random_int(min=16, max=60),
                    "city": faker.city(),
                    "country": faker.country(),
                    "phone": faker.phone_number(),
                    "job": faker.job(),
                }
            }
        }
        users.append(user)
    return users

users = generate_users(5)
for user in users:
    print(json.dumps(user, indent=4, ensure_ascii=False))





