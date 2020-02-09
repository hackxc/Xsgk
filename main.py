#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,os
import mysql.connector
from flask import Flask,render_template,request,flash
from optparse import OptionParser

print (''' __  __          _    
 \ \/ /___  __ _| | __
  \  // __|/ _` | |/ /
  /  \\\\__ \ (_| |   < 
 /_/\_\___/\__, |_|\_\\
           |___/           www.hackxc.cc
''')
mysqllist = []
with open('./config.ini','r') as f:
    for x in f.readlines():
        mysqllist.append(x)
mydb = mysql.connector.connect(
    host = '%s'%mysqllist[2].split(':')[1].strip(),
    user = '%s'%mysqllist[3].split(':')[1].strip(),
    password = '%s'%mysqllist[4].split(':')[1].strip(),
    database = '%s'%mysqllist[5].split(':')[1].strip()
)
global a

def qq(x):
    mycurros = mydb.cursor()
    qq = ("select * from qq where user='%s'"%x)
    #模糊查询：select * from lesson where user like '%123456%' or password like '%123456%'
    mycurros.execute(qq)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u'QQ：{:>50}　　　　　密码：{:>50}'.format(a[x][1], a[x][2]))

def name(x):
    mycurros = mydb.cursor()
    name = ("select * from info where name='%s'"%x)
    mycurros.execute(name)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"姓名：{:>50}　　身份证：{:>50}　　地址：{:>50}　　手机号：{:>50}　　邮箱：{:>50}".format(a[x][1], a[x][2],a[x][3],a[x][4],a[x][5]))

def address(x):
    mycurros = mydb.cursor()
    address = ("select * from info where address='%s'"%x)
    mycurros.execute(address)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"姓名：{:>50}　　身份证：{:>50}　　地址：{:>50}　　手机号：{:>50}　　邮箱：{:>50}".format(a[x][1], a[x][2],a[x][3],a[x][4],a[x][5]))

def iphone(x):
    mycurros = mydb.cursor()
    iphone = ("select * from info where iphone='%s'"%x)
    mycurros.execute(iphone)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"姓名：{:>50}　　身份证：{:>50}　　地址：{:>50}　　手机号：{:>50}　　邮箱：{:>50}".format(a[x][1], a[x][2],a[x][3],a[x][4],a[x][5]))

def sfz(x):
    mycurros = mydb.cursor()
    sfz = ("select * from info where sfz='%s'"%x)
    mycurros.execute(sfz)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"姓名：{:>50}　　身份证：{:>50}　　地址：{:>50}　　手机号：{:>50}　　邮箱：{:>50}".format(a[x][1], a[x][2],a[x][3],a[x][4],a[x][5]))



def email(x):
    mycurros = mydb.cursor()
    email = ("select * from info where email='%s'"%x)
    mycurros.execute(email)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"姓名：{:>50}　　身份证：{:>50}　　地址：{:>50}　　手机号：{:>50}　　邮箱：{:>50}".format(a[x][1], a[x][2],a[x][3],a[x][4],a[x][5]))


def email2(x):
    mycurros = mydb.cursor()
    email2 = ("select * from email where email='%s'"%x)
    mycurros.execute(email2)
    a = mycurros.fetchall()
    for x in range(0, len(a)):
        flash(u"邮箱：{:>50}　　密码：{:>50}".format(a[x][1], a[x][2]))

app = Flask(__name__)
app.secret_key = ('www.hackxc.cc')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        key = request.form.get('key')
        select = request.values.get("select")
        if not all([key]):
            flash (u"请输入你要查询的内容")
        elif key:
            if select == (u"QQ"):
                qq(key)
            elif select == (u"姓名"):
                name(key)
            elif select == (u"地址"):
                address(key)
            elif select == (u"邮箱"):
                email(key)
                email2(key)
            elif select == (u"手机号"):
                iphone(key)
            elif select == (u"身份证"):
                sfz(key)
        else:
            pass
    return render_template('index.html')


if __name__ == '__main__':
    usage = ("usage: %prog -p 8080")
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--port", dest="port", help="Port Setting")
    options, args = parser.parse_args()
    port = options.port
    if port==None:
        print ("Usage : %s -p 8080"%os.path.basename(sys.argv[0]))
        sys.exit(0)
    app.run(port="%s"%port)
