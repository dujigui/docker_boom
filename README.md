# 我可以跑多少个 Docker 容器

本项目纯属无聊，关于此项目的背景请[移步博客](http://www.nullsfootprints.com/post/32)。

## 构建

```
git clone git@github.com:dujigui/docker_boom.git
cd docker_boom/go
docker build -t docker_boom:1.0 .
```

## 查看内存/CPU占用
```
pip install psutil
python3 stat.py
```

## 添加容器

例如 50 个.

```
cd docker_boom/py
python3 add.py 50 docker_boom:1.0
```

## 删除容器

**删除所有正在运行的容器,谨慎使用!!!**

```
cd docker_boom/py
python3 remove.py
```