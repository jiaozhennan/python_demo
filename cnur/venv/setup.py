from distutils.core import setup

setup(
    name='nester',
    version='1.0.0',
    py_modules=['nester'],
    author='jiaozn',
    author_email='jiaozn@163.com',
    url='http://www.jiaozn.com',
    description='A simple printer of nested lists'
)


'''
python 模块

以.py结尾
标准库
PyPi
第三方

'''
注释
'''
#单行注释
模块位置
sys.path

发布
新建一个文件夹nester，模块nester.py放入文件件
新建setup.py
python setup.py sdist
python setup.py install
使用 
import nester
nester.print_lol(cast)
或者
form nester import print_lol as pl
官网注册用户
命令行注册PyPi
python setup.py register
向PyPi上传发布
python setup.py sdist upload
'''