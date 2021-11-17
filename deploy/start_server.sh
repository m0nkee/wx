#! /bin/bash
###
 # @Description: 运行脚本
 # @Author: Monkee Lei
 # @Date: 2021/11/17
### 

pipenv run gunicorn -w 4 'app:create_app()' --daemon
