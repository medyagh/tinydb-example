import tinydb
from tinydb import where, Query
from tinydb.operations import delete
import random

User = Query()


def insert_unquie_recipes(r):
    s=db.search(User.name == r["name"])
    if len(s)>1:
        print ("warning duplicate names")
    elif len(s)>0:
        for k in s[0].keys():
            print (s[0][k])
        print ("Won't insert since key already exists")
    else:
        print ("---"*13)
        print ("inserting"+str(r))
        db.insert(r)


def update_recipe(name):
    el = db.get(User.name == name)
    random.randint(1, 10)
    db.update({'ingredients': random.randint(1, 10)}, eids=[el.eid])


def remove_recipe(name):
    el = db.get(User.name == name)
    db.remove(eids=[el.eid])


db = tinydb.TinyDB("mydb.json")

recipes = [
           {"name":"Pizza", "ingredients":["Pepperoni", "Mushroom", "Tomato","Thin Crust"]},
           {"name":"Soup", "ingredients":["Chicken", "Garlic", "","Carrot","Carrot","Onion"]},
           {"name":"Kelana", "ingredients":["Sawzi", "Butter"]},
           ]

for r in recipes:
    insert_unquie_recipes(r)

update_recipe("Soup")
el = db.all()
print (el)
remove_recipe("Soup")
el = db.all()
print (el)

# x=db.search( where("name") == "Fried Rice" )
# print (x)

# print (db.search(User.name == "Soup")[0]["ingredients"])
