x = {"id" : 100 , "name" : "Saman" , "salary" : 50000.00}

print(x)
print(type(x))

print(x["id"])
print(x["name"])
print(x["salary"])

x["bonus"] = 1000.00
print(x)

x["salary"] = 60000.00
print(x)

x["address"] = {"no" : 51 , "street" : "1st Lane" , "town" : "Kandy"}

x["telephone"] = {"0718567455" , "0778899345"}
print(x)

print(x["address"]["town"])
