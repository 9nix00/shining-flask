How To
==============

目标
--------

- 理解公众号文章中涉及的Migrate运行原理
- 模拟多项目环境，演示如何不冲突的复用表结构


前置依赖
---------
- 全局依赖，参考 [README.md](../README.md)
- docker & docker-compose

快速运行
---------

```
docker-compose -f services.yml up -d
pip install -r ./requirements.txt
cd project-a && python app.py
cd ../project-b && python app.py
```

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

