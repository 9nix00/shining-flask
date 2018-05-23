How To
==============

目标
--------

- 理解公众号文章中涉及的Migrate运行原理
- 模拟多项目环境，演示如何不冲突的复用表结构


Migrate风格DB设计原则
------------------------

以下为风爻建议的一般通用性原则。

- 保持简单

      你应该保持当前DB表结构的简单，不要做过度的设计，尽量*不要*预留字段。
      特别是不太确定是否要添加的字段。
    
- 保持小巧

      在生成Migrate时候，应该尽可能的发挥DB的原子操作特性。
      不要多个表的Migrate混在一起操作。
      在一些极端的情况下，执行Migrate时DB连接会出现中断，
      而利用好Migrate原子特性的Migrate，可以将风险和损失降到最低。

- 保持单一的核心
      
      关系型数据库作为一种经典数据库，作为核心数据库，数据存储应该单一化，突出关系特性。
      做关系型数据库擅长的事情，比如订单、会员资料等是适用于关系型数据库的。
      
      一个简单（粗略但快速的）的判断标准是，你使用到的数据是否需要事务特性。
      
- 拥抱多元的扩展

      现代数据库相比10年前已经出现了极大的演进，仅开源DB据统计就有100种之多。
      对于一些专用数据，风爻建议使用外围DB更合适，如MongoDB，LevelDB，Cassandra等。
      随着云计算的成熟，引入多种DB成本是极低的。


前置依赖
---------
- 全局依赖，参考 [README.md](../README.md)
- docker & docker-compose
- 建议先停止掉本地的Mysql Server使用已配置的docker启动。

快速运行
---------

```
docker-compose -f services.yml up -d
pip install -r ./requirements.txt
cd project-a && python app.py
cd ../project-b && python app.py
```

运行完成后，在DB中查看相关表结构已生效。

如存在依赖缺失，请自行安装，并反馈至公众号。

项目A 使用浏览器访问 [http://127.0.0.1:5000](http://127.0.0.1:5000)
项目B 使用浏览器访问 [http://127.0.0.1:5001](http://127.0.0.1:5001)


DIY
---------

```
# 准备依赖
pip install -r ./requirements.txt
docker-compose -f ./services.yml up -d
rm -rf ./project-*/migrations

# 重建项目A的migrations
cd ./project-a && python manage.py ff makemigrations
printf 'account\ntopic\n' > ./migrations/models.txt
python manage.py ff makemigrations

# 重建项目A的migrations
cd ../project-b && python manage.py ff makemigrations
printf 'account\ntopic\nhello\n' > ./migrations/models.txt
python manage.py ff makemigrations

# 返回父目录，开始执行
cd ../
cd project-a && python app.py
cd ../project-b && python app.py

# 查看数据库表结构
mysql -u root -phello_world -D project_a -h 127.0.0.1 -e 'show tables' | grep account
mysql -u root -phello_world -D project_b -h 127.0.0.1 -e 'show tables' | grep account
```

