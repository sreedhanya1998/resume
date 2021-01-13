f=open("complete.csv","r")
covid_data={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed=data[4]
    death=data[5]
    cured=data[6]
    if state not in covid_data:
        covid_data[state]={
            "state":state,
            "confirmed":confirmed,
            "death":death,
            "cured":cured
        }
    else:
        covid_data[state] = {
            "state": state,
            "confirmed": confirmed,
            "death": death,
            "cured": cured
        }
def print_covid(**kwargs):
    state=kwargs.get("state")
    if state in covid_data:
        print(state,covid_data[state]["confirmed"])
    if state in covid_data:
        if "property" in kwargs:
            prop=kwargs.get("property")
            if prop in covid_data[state]:
                print(prop,covid_data[state][prop])


print_covid(state="Kerala",property="cured")