laptop={"brand":"acer","model":"nitro5","display":"tft","storage":"512gb","fan":"1 fan","price":50000}



print(laptop["model"])
print(laptop["storage"])

print("ram_type" in laptop)
laptop["ram_type"]="8gb"
print(laptop)

laptop["display"]="amoled"
print(laptop)


#  using get() method
print(laptop.get("model"))
print(laptop.get("storage"))



# updating dictionary
if "fan" in laptop:
    laptop="2 fan"
else:
    laptop="1 fan"
print(laptop)



if laptop["price"]>45000:
    laptop["price"]-=1500
else:
    laptop["price"]-=1000
print(laptop)
