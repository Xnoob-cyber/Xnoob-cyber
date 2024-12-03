x = {"name":"john", 'age':14, "city":"edinburgh"} #dictionary
print(x)
y = {"gili", 16, "strike"} #set
z = {"gig", "jertous", "refnses"}
print(y)
# in a dic and set they are  not indexed and store in memory not in orderly manner therefore they cant fetched using index values ex; x[1]
y.add("world") # to add elements add syntax can be used,same elements are not repeated.
y.remove(16) # to remove a element remove syntax can be used.
print(y, "<---new y set")
q = y.union(z) # y+z is not valid in sets but y-z is valid
print(q, "<----sum of sets y and z") 
print(type(y))

p = (124, "jonathon", 25)
height, name, age = p 
print(height, name, age) #we can equal the values into 3 variables in orderly

