framework=[
    ["django","python",4],
    ["flask","python",3],
    ["spring","java",5],
    ["express","javascript",4],
    ["angular","typescript",4]
]

# print python framework
#1st method
for fw in framework:
    if fw[1]=="python":
        print(fw)


#2nd method
pyfw=[fw for fw in framework if fw[1]=="python"]
print(pyfw)