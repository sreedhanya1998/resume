f=open("employe_data","r")
emp_dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    desig=data[2]
    exp=data[3]
    salary=data[4]
    if id not in emp_dict:
        emp_dict[id]={
            "id":id,
            "name":name,
            "desig":desig,
            "exp":exp,
            "salary":salary
        }
    else:
        emp_dict[id] = {
            "id": id,
            "name": name,
            "desig": desig,
            "exp": exp,
            "salary": salary
        }
def print_emp(**kwargs):
    id=kwargs.get("id")
    if(id in emp_dict):
        if "property" in kwargs:
            prop=kwargs.get("propety")
            if prop in emp_dict[id]:
                print(emp_dict[id][prop])

print_emp(id=100,property="desig")