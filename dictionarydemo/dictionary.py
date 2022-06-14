laptop={"brand":"acer","model":"nitro5","display":"tft","storage":"512gb"}
print(laptop["model"])
print(laptop["storage"])

print("ram_type" in laptop)
laptop["ram_type"]="8gb"
print(laptop)

laptop["display"]="amoled"
print(laptop)