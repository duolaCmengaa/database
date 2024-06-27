import os, pandas, random, django
from datetime import date




def user():
    from users.models import User
    if not(User.objects.filter()):
        stu_id = [i+j+k for k in [21000000000,22000000000,23000000000,24000000000] for j in [307110000, 307130000, 300180000] for i in range(100)]
        Roads = ["Avenue", "Street", "Road", "Lane"]
        Cities = ["Tokyo", "Delhi", "Manila", "Sao Paulo", "Guangzhou", "Shanghai", "Beijing", "Los Angeles", "Bangkok",
                  "Seoul", "Buenos Aires", "Paris", "London", "Madrid", "Hong Kong"]
        names = pandas.read_csv(r"playground\names.csv")
        names = list(names['names'])
        for stu in stu_id:
            surname = random.choice(names)
            lastname = random.choice(names)
            User.objects.get_or_create(id=stu,
                                       name=surname + ' ' + lastname,
                                       sex=random.choices(["Male", "Female", "None"], [10, 10, 1], k=1)[0],
                                       phone=random.choice(['189', '186', '137', '191', '158']) + str(
                                           random.randint(10000000, 100000000)),
                                       email=str(stu) + '@fudan.edu.cn',
                                       address=str(random.randint(1, 999)) + ' ' + random.choice(names)[:6] + ' ' +
                                               random.choice(Roads) + ', ' + random.choice(Cities),
                                       vip=random.choice([0, 1]))


def publisher():
    from publishers.models import Publishers
    if not (Publishers.objects.filter()):
        Roads = ["Avenue", "Street", "Road", "Lane"]
        Cities = ["Tokyo", "Delhi", "Manila", "Sao Paulo", "Guangzhou", "Shanghai", "Beijing", "Los Angeles", "Bangkok",
                  "Seoul", "Buenos Aires", "Paris", "London", "Madrid", "Hong Kong"]
        Books = pandas.read_csv(r"data\scraping.csv")
        names = pandas.read_csv(r"playground\names.csv")
        names = list(names['names'])
        user = []
        for item in Books['publisher'].drop_duplicates():
            surname = random.choice(names)
            lastname = random.choice(names)
            Publishers.objects.get_or_create(name=item,
                                             phone_number=random.choice(['189', '186', '137', '191', '158']) + str(
                                                 random.randint(10000000, 100000000)),
                                             email=surname + random.choice(
                                                 ['@163.com', '@gmail.com', '@qq.com', '@hotmail.com', '@126.com']),
                                             contacts=surname + ' ' + lastname,
                                             address=str(random.randint(1, 999)) + ' ' + random.choice(names)[:8] + ' ' +
                                                     random.choice(Roads) + ', ' + random.choice(Cities),
                                             )


def writer():
    from writers.models import Writers
    if not (Writers.objects.filter(author_type="Author")):
        Books = pandas.read_csv(r"data\scraping.csv")
        for item in Books['author'].drop_duplicates():
            Writers.objects.get_or_create(name=item,
                                          author_type="Author"
                                          )
    if not (Writers.objects.filter(author_type="Translator")):
        Books = pandas.read_csv(r"data\translators.csv")
        for item in Books['translator'].drop_duplicates():
            Writers.objects.get_or_create(name=item,
                                          author_type="Translator"
                                          )


def classification():
    from books.models import Classification, ClassificationSub
    Books = pandas.read_csv(r"data\scraping.csv")
    if not (Classification.objects.filter()):
        for item in Books['category1'].drop_duplicates():
            Classification.objects.get_or_create(class_name=item)
    if not (ClassificationSub.objects.filter()):
        for item in Books[['category1', 'category2']].drop_duplicates().itertuples():
            ClassificationSub.objects.get_or_create(class_name=item[2],
                                                    ancestor_class_name=Classification.objects.get(class_name=item[1]))


def book():
    from books.models import Classification, ClassificationSub, Books
    from writers.models import Writers
    from publishers.models import Publishers
    books = pandas.read_csv(r"data\scraping.csv")
    translators = pandas.read_csv(r"data\translators.csv")
    if not (Books.objects.filter()):
        for item in books.drop_duplicates().itertuples():
            book = Books.objects.get_or_create(title=item[1],
                                               price=float(item[3]),
                                               price_vip=float(item[3]) * random.choice([0.7, 0.8, 0.9]),
                                               publish_date=date(int(item[4]), random.randint(1, 12),
                                                                 random.randint(1, 28)),
                                               publishers=Publishers.objects.get(name=item[5]),
                                               edition=item[6],
                                               classification=Classification.objects.get(class_name=item[7]),
                                               sub_classification=ClassificationSub.objects.get(class_name=item[8]),
                                               storage=str(random.randint(10, 200)))
            book = book[0]
            if Writers.objects.get(name=item[2], author_type='Author'):
                book.writers.add(Writers.objects.get(name=item[2], author_type='Author'))
            if len(item[2]) > 3:
                translator = random.choice(list(translators['translator']))
                if Writers.objects.get(name=translator, author_type='Translator'):
                    book.writers.add(Writers.objects.get(name=translator, author_type='Translator'))


def populate_stores():
    from store.models import Store
    if not (Store.objects.filter()):
        Roads = ["Avenue", "Street", "Road", "Lane"]
        Cities = ["Tokyo", "Delhi", "Manila", "Sao Paulo", "Guangzhou", "Shanghai", "Beijing", "Los Angeles", "Bangkok",
                  "Seoul", "Buenos Aires", "Paris", "London", "Madrid", "Hong Kong"]
        names = pandas.read_csv(r"playground\names.csv")
        names = list(names['names'])

        store_prefixes = [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
            "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
            "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", 
            "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington","shanghai","beijing","fudan","qingdao",
            "guilin","luoyang","jilin","chengdu"
        ]

        store_suffixes = [" Store No. 1", " Store No. 2", " Store No. 3", " Store No. 4", " Store No. 5"," Store No. 6"," Store No. 7"," Store No. 8"," Store No. 9"," Store No. 10"," Store No. 11"," Store No. 12"," Store No. 13"," Store No. 14"," Store No. 15"," Store No. 16"," Store No. 17"," Store No. 18"," Store No. 19"," Store No. 20"]
        
        generated_names = set()
        max_names = 150

        while len(generated_names) < max_names:
            prefix = random.choice(store_prefixes)
            suffix = random.choice(store_suffixes)
            name = prefix + suffix
            generated_names.add(name)

        # Convert set to list for shuffling
        generated_names = list(generated_names)

        # Shuffle the list to mix original and generated names
        random.shuffle(generated_names)


        for store_name in generated_names:
            manager_first_name = random.choice(names)
            manager_last_name = random.choice(names)
            Store.objects.get_or_create(
                name=store_name,
                location=f"{random.randint(1, 999)} {random.choice(names)[:8]} {random.choice(Roads)}, {random.choice(Cities)}",
                phone_number=random.choice(['189', '186', '137', '191', '158']) + str(random.randint(10000000, 99999999)),
                manager=f"{manager_first_name} {manager_last_name}",
            )




# 修改2

def supply():
    from supplier.models import Supplier
    if not (Supplier.objects.filter()):
        Roads = ["Avenue", "Street", "Road", "Lane"]
        Cities = ["Tokyo", "Delhi", "Manila", "Sao Paulo", "Guangzhou", "Shanghai", "Beijing", "Los Angeles", "Bangkok",
                  "Seoul", "Buenos Aires", "Paris", "London", "Madrid", "Hong Kong"]
        names = pandas.read_csv(r"playground\names.csv")
        names = list(names['names'])

        supply_prefixes = [
            "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
            "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
            "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", 
            "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington",
            "Shanghai", "Beijing", "Fudan", "Qingdao", "Guilin", "Luoyang", 
            "Jilin", "Chengdu", "Heze", "Tokyo", "Delhi", "Manila", "Sao Paulo", 
            "Guangzhou", "Bangkok", "Seoul", "Buenos Aires", "Paris", "London", 
            "Madrid", "Hong Kong", "Moscow", "Berlin", "Rome", "Cairo", 
            "Istanbul", "Sydney", "Melbourne", "Toronto", "Vancouver", 
            "Mexico City", "Mumbai", "Kolkata", "Lagos", "Johannesburg", 
            "Cape Town", "Dubai", "Kuala Lumpur", "Singapore", "Zurich", 
            "Geneva", "Vienna", "Budapest", "Warsaw", "Prague", "Helsinki",
            "Stockholm", "Oslo", "Copenhagen", "Brussels", "Amsterdam", 
            "Dublin", "Lisbon", "Barcelona", "Athens", "Bangkok", "Taipei",
            "Krakow", "Buenos Aires", "Lima", "Santiago", "Bogota", 
            "Caracas", "Havana", "Santo Domingo", "Montevideo", "Quito",
            "Kingston", "Port-au-Prince"
        ]

        supply_suffixes = [" Company", " Supplier", " Supply", " Provider", " Vendor"]
        generated_names = set()
        max_names = 150

        while len(generated_names) < max_names:
            prefix = random.choice(supply_prefixes)
            suffix = random.choice(supply_suffixes)
            name = prefix + suffix
            generated_names.add(name)

        # Convert set to list for shuffling
        generated_names = list(generated_names)

        # Shuffle the list to mix original and generated names
        random.shuffle(generated_names)


        for supply_name in generated_names:
            first_name = random.choice(names)
            last_name = random.choice(names)
            Supplier.objects.get_or_create(
                name=supply_name,
                phone_number=random.choice(['189', '186', '137', '191', '158']) + str(random.randint(10000000, 99999999)),
                email=first_name + random.choice(['@163.com', '@gmail.com', '@qq.com', '@hotmail.com', '@126.com']),
                contact_person=f"{first_name} {last_name}",
                address=f"{random.randint(1, 999)} {random.choice(names)[:8]} {random.choice(Roads)}, {random.choice(Cities)}"
            )

# 修改3
def assign_suppliers_to_stores():
    from store.models import Store
    from supplier.models import Supplier

    stores = Store.objects.all()
    suppliers = list(Supplier.objects.all())
    for store in stores:
        num_suppliers = random.randint(1, 5)  # 每个 Store 分配 1 到 5 个 Supplier
        store_suppliers = random.sample(suppliers, num_suppliers)
        store.suppliers.set(store_suppliers)





def order_data():
    from django.shortcuts import render, redirect
    from login.models import User as login1
    from users.models import User as Customer
    from books.models import Books
    from orders.models import Orders, Details
    import random, time, datetime
    from django.utils import timezone
    from store.models import Store
    from random import choice
    from datetime import datetime, timedelta
    import random
    from django.utils import timezone
    
    num = random.randint(90, 100)
    for i in range(num):
        init_time = ''.join(str(time.time()).split('.'))
        time.sleep(0.01)
        user = random.choice(list(Customer.objects.all()))

        # 获取 Store 模型中的所有记录
        all_stores = Store.objects.all()

        # 随机选择一个 Store 实例
        store = choice(all_stores) 

        loginmember = random.choice(list(login1.objects.all()))


        # 过去一年的随机日期
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1095)

        random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))


            # 获取第一个店铺作为默认值，你可以根据实际情况修改这里
        new, created = Orders.objects.get_or_create(id=init_time,
                                                    date=random_date,
                                                    user=user,
                                                    store=store,
                                                    confirm='1',
                                                    lastedit = loginmember
                                                    )
        for j in range(random.randint(1, 5)):
            book = random.choice(list(Books.objects.all()))
            if user.vip == 1:
                bookprice = book.price_vip
            else:
                bookprice = book.price
            Details.objects.create(book=book,
                                    order=new,
                                    price=bookprice,
                                    count=random.randint(1, 20))





    
def user_data():
    from login.models import User
    if not (User.objects.filter()):
        nums = 10
        for i in range(nums):
            first_name = random.choice(["管理员1","管理员2","管理员3","管理员4"])
            last_name = random.choice(["A","B","C","D","E"])

            names = pandas.read_csv(r"playground\names.csv")
            names = list(names['names'])
 
            surname = random.choice(names)
                
            User.objects.get_or_create(
                username=f"{first_name} {last_name}",
                email=surname + random.choice(['@163.com', '@gmail.com', '@qq.com', '@hotmail.com', '@126.com']),
                pwd=random.choice(['123456', '123456789', '456789', 'a123465']),
                ip=random.choice(['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4'])
            )











def main():
    user()
    publisher()
    writer()
    classification()
    book()
    populate_stores()
    supply()
    assign_suppliers_to_stores()
    user_data()
    order_data()










if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BookStoreDB.settings")
    if django.VERSION >= (1, 7):
        django.setup()
    main()
    print("done!")
