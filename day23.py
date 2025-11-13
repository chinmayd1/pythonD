students = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":36,
        "skills":["python","sql"],
        "marks":{"maths":95,"science":97,"english":77}
    },
    {
        "firstName":"mayuri",
        "lastName":"rao",
        "age":37,
        "skills":["python","sql","c"],
        "marks":{"maths":95,"science":92,"english":70}
    },
    {
        "firstName":"amol",
        "lastName":"deshmukh",
        "age":35,
        "skills":["python","sql","django"],
        "marks":{"maths":55,"science":92,"english":75}
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":32,
        "skills":["python"],
        "marks":{"maths":92,"science":44,"english":76}
    }

]

#firstName of all students
for x in students:
    print(x['firstName'])

#firstName:numberofSkills
for x in students:
    e = str(len(x['skills']))
    print(f'{x['firstName']}:{e}')

# firstName + totalNumber of marks 

for x in students:
    total = x['marks']['maths'] +x['marks']['science']+x['marks']['english']
    total = str(total)
    print(x['firstName']+" "+total)


