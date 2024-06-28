# BookStoreDB

#### 网上综合书店销售数据库

# Target
设计并实现一个综合性的数据库系统，用于管理连锁销售公司的门店、商品（包
括图书）、供货商、客户（包括会员）、销售记录及统计数据。

- [BookStoreDB](#bookstoredb)
  - [Versions](#versions)
  - [Compatibility](#compatibility)
  - [使用说明](#使用说明)
    - [1 安装与部署](#1-安装与部署)
    - [2. 注册与登录](#2-注册与登录)
    - [3.超级管理员](#3超级管理员)
    - [4.主页](#4主页)
      - [4.1 Users](#41-users)
      - [4.2 Publishers](#42-publishers)
      - [4.3 Writers](#43-writers)
      - [4.4 Books](#44-books)
      - [4.5 Orders](#45-orders)
      - [4.6 Stores](#46-stores)
      - [4.7 Suppliers](#47-suppliers)
  - [Contributors](#contributors)
  - [Database Schema](#database-schema)
    - [Login\_user](#login_user)
    - [Users\_user](#users_user)
    - [Publishers\_publishers](#publishers_publishers)
    - [Writers\_writers](#writers_writers)
    - [Books\_books](#books_books)
    - [Books\_books\_writers](#books_books_writers)
    - [Books\_classification](#books_classification)
    - [Books\_classificationsub](#books_classificationsub)
    - [Orders\_orders](#orders_orders)
    - [Orders\_details](#orders_details)
    - [Store\_store](#store_store)
    - [Supplier\_supplier](#supplier_supplier)
    - [Store\_store\_suppliers](#store_store_suppliers)
  - [URL paths](#url-paths)
  - [Design Documents](#design-documents)
    - [1 系统需求分析](#1-系统需求分析)
      - [1.1 用户需求分析](#11-用户需求分析)
      - [1.2 功能设计](#12-功能设计)
    - [2  模型图](#2--模型图)
      - [2.1 数据流图](#21-数据流图)
      - [2.2  数据字典](#22-数据字典)
      - [2.3  E-R图](#23--e-r图)
    - [3   功能划分](#3---功能划分)
      - [3.1  管理员登录、注册功能](#31--管理员登录注册功能)
      - [3.2  检索功能](#32--检索功能)
      - [3.3  修改/删除功能](#33--修改删除功能)
      - [3.4  订单操作](#34--订单操作)
            

## Versions

|    Artifact     | Version  |
|:---------------:|:--------:|
|      MySQL      |  8.0.23  |
|     Python      |  3.7.10  |
| Navicat Premium | 15.0.023 |
|     Django      |  3.2.3   |
|     Pymysql     |  1.0.2   |
|    Bootstrap    |   4.5    |

## Compatibility

BookStoreDB works on Windows 10&11. Chrome is recommended to have the best experience.

## 使用说明

### 1 安装与部署

1. Git clone through Git CMD or download the project through Github Desktop to your direction:

```
git clone https://github.com/duolaCmengaa/database.git
cd database-main
```
2. Enter the root file "BookStoreDB/" and install dependencies:

  ```
  pip install -r requirements.txt
  ```

3. Set up database and replace my username and password in project root file "BookStoreDB/settings.py" containing something like:

  ```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "BookStoreDB",
        'USER': username,
        'PASSWORD': password,
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
  ```

4. Apply migrations and create superuser:
  ```cmd
  python manage.py migrate
  python manage.py createsuperuser # Not necessarily required.
  ```

5. To avoid starting the system with empty database, run in command line:
```cmd
  python data.py
```

6. Start server at local host:
```cmd
  python manage.py runserver # Following message will occur.
```

```cmd
System check identified no issues (0 silenced).
June 25, 2024 - 21:14:51
Django version 4.2.13, using settings 'BookStoreDB.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

7. Enter server:  http://127.0.0.1:8000/
   
8. Database being polluted, you may:

```python
  python manage.py flush
  python data.py  # This simply reset everything including your login info.
```

### 2. 注册与登录

进入BookStoreDB导航页，点击Start按钮，进如用户注册/登录界面。

![image](https://github.com/duolaCmengaa/database/assets/145974277/4c2bc4a6-c3ce-4844-810b-1ff36024d0ae)

如果没有账号可以先进行注册，填写完id、邮箱、密码后进行注册，注册完成后返回登录界面，已有账号的用户可以直接进行登录。

![image](https://github.com/duolaCmengaa/database/assets/145974277/47aa5654-40be-4892-9574-bcedd5878adb)
  
![image](https://github.com/duolaCmengaa/database/assets/145974277/0d378e31-1bd7-424a-b334-faf1e8313f60)


### 3.超级管理员

通过连接 http://127.0.0.1:8000/admin ，进入超级管理员登录界面。通过输入在“python manage.py createsuperuser”命令后设置的账户和密码，进入超管控制面板。在超级管理员控制面板可以对管理员、书籍、门店、供货商等进行编辑。

![image](https://github.com/duolaCmengaa/database/assets/145974277/09204a39-dcab-4f7e-9c92-d8d30dd172a2)



### 4.主页

在BookStoreDB主页，可以获取新订单，每次获得的订单数在5-10之间。此外点击不同标签页可以获取不同信息。

![image](https://github.com/duolaCmengaa/database/assets/145974277/dda8bf01-1727-4f48-9edc-14f6bb36704f)



#### 4.1 Users

在Users标签页，可以浏览当前所有用户，用户分为VIP和普通用户，可以对每个用户进行编辑和删除。除此之外，可以通过输入用户id、地址、邮箱、姓名等进行查找，并可通过ID、姓名的等对用户进行排序（升序/降序）。

![image](https://github.com/duolaCmengaa/database/assets/145974277/ea1320d8-3bd9-495a-b655-134d8be9b3d8)

#### 4.2 Publishers

在Publishers界面可以查看出版商信息，包含出版商名称、联系电话、邮箱、联系人、地址，并可对出版商信息进行编辑和删除。另外，可以根据出版商名称、地址、邮件、id等进行查找和升降序排序。

#### 4.3 Writers

在Writers页面可以查看作者信息，包含作家姓名和类别（作者/译者）。可以通过姓名和ID进行查找和排序、根据作家类别进行分类。同时可以对每条作家信息进行编辑和删除。

![image](https://github.com/duolaCmengaa/database/assets/145974277/ba596d5f-a955-49f7-bb5d-af855f0ac1a0)

#### 4.4 Books

在Books标签页可以看到每本书的标题、作者、价格（普通价格/VIP价格）、出版商、图书类别/子类别、出版日期、版本、库存等信息，可以根据图书的ID、标题、作者、出版商、类别、子类等进行查找和分类，并且可以对每本书的信息进行编辑和删除

#### 4.5 Orders

在Orders标签页可以看到每条订单的ID、订单日期、门店、订单客户、订单书籍以及相对应的数量和单价。每条订单可以被确认，未被确认的订单可以被修改或删除以防止恶意订单，被确认的订单会显示确认订单的用户名。可以通过OrderID、订单客户、订单日期、门店名以及确认订单的用户名进行查找，通过是否被确认进行分类筛选，以及根据各个指标对订单进行排序。

![image](https://github.com/duolaCmengaa/database/assets/145974277/a2fdceb3-58c4-4d3f-bf13-a28a774a807d)

除此之外，可以通过“Order Summary and Analysis”按钮进入订单汇总界面。里面展示时间段内的订单总数、售出图书总量以及总销售额，同时会显示在时间段内每个门店的总图书销量和销售额，图书的销量排行榜，用户的购买量的排行榜，可以选择汇总的开始、结束日期以进行筛选。

![image](https://github.com/duolaCmengaa/database/assets/145974277/b64532b9-19bd-45d0-87b5-38845707d756)

#### 4.6 Stores

在Stores标签页可以看到每个门店的ID、名称、地址、联系电话、经理姓名和对应供货商。可以通过门店名、地址、联系电话和经理姓名对门店进行查找和排序。同时可以对每个门店的信息进行编辑和删除。

![image](https://github.com/duolaCmengaa/database/assets/145974277/91e037a5-8500-43ce-8168-e4341e0680eb)

#### 4.7 Suppliers

在Suppliers标签页可以看到每个供货商的ID、名称、联系电话、电子邮箱、联系人和地址。可以通过供货商名称、联系电话、联系人、电子邮件进行查找和排序。可以对每条门店的信息进行单独编辑和删除。

![image](https://github.com/duolaCmengaa/database/assets/145974277/01619d80-d7f9-4838-a641-2e5a47f0449b)

## Contributors

- 乔一宸 
- 马骎 
- 李波 

## Database Schema


### Login_user

| Field    | Type         | Null | Key | Default | Extra          |
|----------|--------------|------|-----|---------|----------------|
| id       | bigint       | NO   | PRI | NULL    | auto_increment |
| username | varchar(40)  | NO   |     | NULL    |                |
| email    | varchar(40)  | NO   |     | NULL    |                |
| pwd      | varchar(128) | NO   |     | NULL    |                |
| ip       | varchar(40)  | NO   |     | NULL    |                |


### Users_user
| Field   | Type         | Null | Key | Default | Extra          |
|---------|--------------|------|-----|---------|----------------|
| id      | bigint       | NO   | PRI | NULL    | auto_increment |
| name    | varchar(40)  | NO   |     | NULL    |                |
| sex     | varchar(6)   | NO   |     | NULL    |                |
| phone   | varchar(20)  | NO   |     | NULL    |                |
| email   | varchar(40)  | NO   |     | NULL    |                |
| vip     | tinyint(1)   | NO   |     | NULL    |                |
| address | varchar(100) | NO   |     | NULL    |                |

### Publishers_publishers

| Field        | Type         | Null | Key | Default | Extra          |
|--------------|--------------|------|-----|---------|----------------|
| id           | bigint       | NO   | PRI | NULL    | auto_increment |
| name         | varchar(100) | NO   |     | NULL    |                |
| phone_number | varchar(20)  | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| contacts     | varchar(40)  | NO   |     | NULL    |                |
| address      | varchar(60)  | NO   |     | NULL    |                |

### Writers_writers

| Field       | Type        | Null | Key | Default | Extra          |
|-------------|-------------|------|-----|---------|----------------|
| id          | bigint      | NO   | PRI | NULL    | auto_increment |
| name        | varchar(40) | NO   |     | NULL    |                |
| author_type | varchar(20) | NO   |     | NULL    |                |

### Books_books

| Field                 | Type         | Null | Key | Default | Extra          |
|-----------------------|--------------|------|-----|---------|----------------|
| id                    | bigint       | NO   | PRI | NULL    | auto_increment |
| title                 | varchar(64)  | NO   | MUL | NULL    |                |
| price                 | decimal(6,2) | NO   |     | NULL    |                |
| price_vip             | decimal(6,2) | NO   |     | NULL    |                |
| publish_date          | date         | NO   |     | NULL    |                |
| edition               | longtext     | YES  |     | NULL    |                |
| storage               | int unsigned | NO   |     | NULL    |                |
| classification_id     | bigint       | NO   | MUL | NULL    |                |
| publishers_id         | bigint       | NO   | MUL | NULL    |                |
| sub_classification_id | bigint       | NO   | MUL | NULL    |                |


### Books_books_writers

| Field      | Type   | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id         | bigint | NO   | PRI | NULL    | auto_increment |
| books_id   | bigint | NO   | MUL | NULL    |                |
| writers_id | bigint | NO   | MUL | NULL    |                |

### Books_classification

| Field      | Type        | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id         | bigint      | NO   | PRI | NULL    | auto_increment |
| class_name | varchar(20) | NO   |     | NULL    |                |

### Books_classificationsub

| Field                  | Type        | Null | Key | Default | Extra          |
| :---- | ---- | ---- | ---- | ------- | ----- |
| id                     | bigint      | NO   | PRI | NULL    | auto_increment |
| class_name             | varchar(20) | NO   |     | NULL    |                |
| ancestor_class_name_id | bigint      | NO   | MUL | NULL    |                |

### Orders_orders

| Field     | Type        | Null | Key | Default | Extra |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id        | varchar(64) | NO   | PRI | NULL    |       |
| last_edit | datetime(6) | NO   |     | NULL    |       |
| date      | date        | NO   |     | NULL    |       |
| user_id   | bigint      | NO   | MUL | NULL    |       |
| store_id  | int         | NO   | MUL | NULL    |       |
| confirm   | varchar(1)  | NO   |     | NULL    |       |

### Orders_details

| Field    | Type         | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id       | bigint       | NO   | PRI | NULL    | auto_increment |
| price    | decimal(6,2) | NO   |     | NULL    |                |
| count    | int unsigned | NO   |     | NULL    |                |
| book_id  | bigint       | NO   | MUL | NULL    |                |
| order_id | varchar(64)  | NO   | MUL | NULL    |                |

### Store_store
| Field    | Type         | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id       | int           | NO  | PRI | NULL    | auto_increment |
| name     | varchar(100)  | NO  |     | NULL    |                |
| location | varchar(200)  | NO  |     | NULL    |                |
| phone_number| varchar(20)| NO  |     | NULL    |                |
| manager  | varchar(100)  | NO  |     | NULL    |                |

### Supplier_supplier
| Field    | Type         | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id       | int           | NO  | PRI | NULL    | auto_increment |
| name     | varchar(100)  | NO  |     | NULL    |                |
| phone_number | varchar(20)  | NO  |   | NULL    |                |
| email| varchar(40)| NO  |     | NULL    |                |
| contact_person  | varchar(40)  | NO  | | NULL    |              |
| address  | varchar(200)  | NO  | | NULL    |              |

### Store_store_suppliers
| Field    | Type         | Null | Key | Default | Extra          |
| ----- | ---- | ---- | ---- | ------- | ----- |
| id           | bigint | NO  | PRI    | NULL    | auto_increment |
| store_id     | int    | NO  | MUL    | NULL    |                |
| supplier_id  | int    | NO  | MUL    | NULL    |                |

## URL paths

The URL tree should be constructed as follows:

```
    1. admin/
    2. accounts/
    3. home/
    4. 
    5. users/
    6. books/
    7. publishers/
    8. writers/
    9. orders/
    10.suppliers/
    11.stores/
    
```

-----

###  后端 API 说明

本项目是基于Django来实现的，

对于一个综合书店销售数据库来说，整个系统的后端 API 说明可以概述如下：

文件说明：

- \__init__.py

用于将包含的目录标记为一个 Python 包。通常为空，但可以用于包的初始化设置。

- admin.py

注册数据库模型以便通过 Django 管理界面进行管理和操作。这可以包括书籍、订单、客户、出版社等模型。

- apps.py

配置应用程序的元数据，如应用名称和配置类，确保应用程序正确加载和配置。

- models.py

定义数据库模型，描述书店的各种数据结构。这些模型包括书籍、作者、分类、订单、客户、出版社等。每个模型对应数据库中的一张表，包含字段和数据类型定义。

- urls.py

定义 URL 路由，将不同的 URL 路径映射到相应的视图函数或类。这使得系统能够正确处理不同的 HTTP 请求，如查看书籍详情、下订单等。

- views.py

包含处理请求的视图函数或类，这些函数或类负责处理来自前端的请求并返回相应的响应。它们执行业务逻辑，如查询数据库、处理表单数据、返回 HTML 页面或 JSON 数据。


###  数据库访问逻辑

数据库访问逻辑主要通过 Django 的 ORM 实现，以下是一些关键点：

- 模型查询

使用模型类来查询数据库。例如，查询所有书籍、某个分类下的书籍或某个客户的订单等。

模型实例操作

- 创建、更新和删除模型实例。

例如，添加新书籍、更新订单状态、删除客户信息等。

- 关联查询

处理模型之间的关系查询。例如，获取某本书的作者信息，获取某个订单的所有书籍明细等。

- 事务管理

在处理复杂操作时，使用数据库事务确保数据一致性。例如，在下订单时，同时减少库存数量和记录订单信息，确保两个操作要么同时成功要么同时失败。


###  前端说明：

我们使用的是Bootstrap框架，Bootstrap 是一个用于开发响应式和移动优先网页的前端框架， 包含了大量的 CSS 和 JavaScript 组件，使得开发者可以快速构建现代、响应式的网站和应用。
我们使用template来渲染动态内容。利用Bootstrap进行响应式和现代化的UI设计。包含导航(navigation)和交互元素以与后端数据进行交互。

------

## Design Documents

### 1 系统需求分析

#### 1.1 用户需求分析

数字化时代的来临改变了人们获取信息和购物的方式，传统的线下书店销售模式显然已经无法满足当代消费者的需求，“亚马逊”，“当当网”逐渐步入人们的生活。因此，建立网上综合书店销售数据库至关重要。数据驱动决策，建立销售数据库可以收集并分析客户行为数据，为书店提供精准的营销策略和个性化的推荐服务。此外，通过网上销售，书店可以跨越地域限制，拓展潜在客户群体，实现更广泛的市场覆盖。总之，建立网上综合书店销售数据库是适应数字化时代趋势的重要举措，所以，本小组设计网上综合书店销售数据库BookStoreDB来作为此次课程项目内容。

#### 1.2 功能设计

首先作为信息管理系统，BookStoreDB将会储存各种数据，包括门店，供货商，商品，图书，客户，会员，销售记录，出版社信息，此外，图书还将被分类,每一类图书还设有子类，作者和译者可能由多人组成，因而还需要额外的作者-译者信息

管理员有更多的权限和责任，他们拥有独立的登录窗口，可以管理供应商信息，门店信息，出版社信息，商品信息，包括添加、修改、查询和删除，以及查看并修改商品库存。管理员还需要管理图书的分类、出版社及作者信息。管理员还可以管理销售记录，包括查看订单信息并审核是否通过，而且他们有权限实现客户信息及会员信息的增加、删除、修改和查询功能。并且管理员需要实现销售记录的录入、修改和查询功能，提供销售数据的汇总和分析。此外设置超管员，拥有最高权限，可以管理管理员信息。

用户具有独立的信息（用户名、姓名、联系电话、e-mail、地址、密码），而且分为会员与非会员两种类型，会员能够享受自己的优惠政策。用户可以在网上浏览商品信息，搜索商品，使用筛选器分类查找目标商品，将商品添加到购物车并进行购买，但是购买的商品量不能超过物品的库存。用户也能够管理自己的个人信息和查看订单历史。综上所述，用户可以通过网上平台轻松完成购物并管理个人信息。

### 2  模型图

#### 2.1 数据流图
![image](https://github.com/duolaCmengaa/database/assets/145974277/c7d70a43-98e6-4a2b-8200-13f77af92dd1)


#### 2.2  数据字典

1. 会员
   1. {用户名，用户的唯一编号，char(30)}
   2. {会员姓名，varchar(10)}
   3. {性别，ENUM(“男”, ”女”, ”保密”)}
   4. {手机号码，varchar(20)}
   5. {email，varchar(30)}
   6. {地址，varchar(50)}
   7. {会员，ENUM(“是”, ”否”)}

2. 管理员
   1. {用户名，管理员的唯一编号，char(30)}
   2. {email，varchar(30)}
   3. {登陆密码，char(128)}

3. 订单信息
   1. {订单号，唯一确定订单的编号，char(10)}
   2. {订单日期，DATETIME}
   3. {收货人姓名，varchar(10)}
   4. {发货状态，ENUM(“未发货”, ”已发货”)}
   5. {图书编号，char(20)}
   6. {订购数量，int(4)}
   7. {单价，int(4)}

4. 图书信息
   1. {图书编号，唯一标识图书的编号，char(20)}
   2. {图书名，varchar(30)}
   3. {出版时间，DATETIME}
   4. {版本号，char(30)}
   5. {出版社编号，int(4)}
   6. {作者/译者编号，int(4)}
   7. {图书类别编号，int(4)}
   8. {图书子类编号，int(4)}
   9. {库存量，int(4)}
   10. {单价，int(4)}
   11. {会员单价，int(4)}

5. 作者/译者
   1. {作者/译者编号，唯一标识作者/译者的编号，int(4)，AUTO_INCREMENT}
   2. {作者/译者名字，varchar(30)}
   3. {作者/译者，SET(“作者“，”译者”)}

6. 出版社信息
   1. {出版社编号，唯一标识出版社的编号，int(4)，AUTO_INCREMENT}
   2. {出版社，varchar(30)}
   3. {出版社地址，varchar(50)}
   4. {出版社email，char(30)}
   5. {出版社联系方式，varchar(20)}

7. 分类信息1
   1. {图书类别编号，唯一标识分类的编号，int(4)，AUTO_INCREMENT}
   2. {类别，varchar(10)}
8. 分类信息2
   1. {图书子类编号，唯一标识子类的编号，int(4)，AUTO_INCREMENT}
   2. {子类，varchar(10)}

#### 2.3  E-R图

![image](https://github.com/duolaCmengaa/database/assets/145974277/93708174-befc-49b4-a228-ca080977de51)

### 3   功能划分

#### 3.1  管理员登录、注册功能

管理员将可以自行录入，设置密码、用户名、email等个人信息，并且密码将使用加密算法，以提高系统的安全性等级。此外设置超级管理员，以对管理员账户及其他信息进行管理。

#### 3.2  检索功能

管理员将被允许使用过滤器、搜索栏，按照分类、关键词、作者、出版社等重要信息对图书进行检索，同时还可以按照销售量、访问量、价格等参数升序或降序排列。管理员还可以单独访问作者、译者以及出版社的具体信息，以便更好地查询信息。

#### 3.3  修改/删除功能

管理员将被允许新增、删除、修改客户、图书、作者、出版社等信息。

#### 3.4  订单操作

订单将会成交当且仅当管理员审核并通过订单，否则可能会导致恶意订单的提交。管理员还被允许根据实际情况增删库存信息以及图书信息。
