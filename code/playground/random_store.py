import random
import pandas
import os

store_ids = [i for i in range(1, 1001)]


Roads = ["Avenue", "Street", "Road", "Lane"]
Cities = [
    "Tokyo",
    "Delhi",
    "Manila",
    "Sao Paulo",
    "Guangzhou",
    "Shanghai",
    "Beijing",
    "Los Angeles",
    "Bangkok",
    "Seoul",
    "Buenos Aires",
    "Paris",
    "London",
    "Madrid",
    "Hong Kong",
]


names = pandas.read_csv("playground/names.csv")
names = list(names["names"])

store = []

for id in store_ids:
    surname = random.choice(names)
    lastname = random.choice(names)
    companyname = random.choice(names)
    store.append(
        [
            id,
            companyname,
            str(random.randint(1, 999))
            + " "
            + random.choice(names)[:8]
            + " "
            + random.choice(Roads)
            + ", "
            + random.choice(Cities),
            random.choice(["189", "186", "137", "191", "158"])
            + str(random.randint(10000000, 100000000)),
            surname + " " + lastname,
        ]
    )

store = pandas.DataFrame(
    store, columns=["Store ID", "Store Name", "Location", "Phone", "Manager"]
)


# Generate a list of 5 random stores
print(store)
store.to_csv("data/stores.csv")
