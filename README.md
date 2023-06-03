# 储蓄保险账户实验系统

## 一、环境要求

python 3.6或3.7（建议通过conda安装python虚拟环境）

python安装完成后，使用pip install -r requirements.txt命令，安装所需依赖库

## 二、本地部署

非常easy，直接python manage.py runserver

然后去浏览器打开http://127.0.0.1:8000/本地地址就可以看到页面和操作了

## 三、上线部署

注意：上线会有样式问题，需要python manage.py collectstatic一下，再将文件传到服务器中

接下来就是一堆的服务器配置，具体是啥我也忘记了。。参考官方文档

