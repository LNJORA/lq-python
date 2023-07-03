#list datastructure tryout
myclassmate=["sharook", "shackro", "arel", "akol","obren"]
myno=[42, 24, 18, 8, 4, 2, -2]
myclassmate[0]="shadrack"
myno.sort()

myclassmate.append("sharon")
myclassmate.insert(2, "telo")
myclassmate.pop(3)
print(myclassmate)
print(myno)

for names in myclassmate:
    print(names)

#tuples--cannot change its positions
countries =("kenya", "southsudan","rwanda", "southafrica", "egypt")
print(countries)
for y in countries:
    print(y)
#datastrcture ..set--start with{}, change with every run done , cannot have two identical number on one set(cannot print an output of the same name)

cars={"toyota" , "honda", "tesla","range rover"}
print(cars)
for c in cars:
    print(c)

#dictionaries data structure

matunda={
    "price":50,
    "color":"green",
    "name":"banana"
}

print(matunda)
x=matunda["name"]
print(x)

carprice={
    "name":"tesla",
    "color":"blue",
    "price":3.8,

}
carprice.pop("price")
carprice["length"]="600m"
carprice.update()
carprice["name"]="lambo"

print(carprice)
t=carprice["name"]
print(t)
for this in carprice:
    print(this)

