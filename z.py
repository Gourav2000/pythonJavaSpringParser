import json

with open('output.json', 'r') as file:
    data = json.load(file)
    classes_interfaces=data
for i in classes_interfaces:
    print("#######################")
    print(i)
    print("#######################")
    for j in classes_interfaces[i]:
        print("*******************************************")
        print(j,end="------------------------------------------------------------->\n")
        print("*******************************************")
        print(classes_interfaces[i][j])
        print("________________________________________________________________________")