from MySQLdb.cursors import DictCursor
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import random
import pymysql

# Create your views here.
def index(request) :
    return render(request, 'star/index.html')

def to_db(request):
    user_rate = pymysql.connect(
        user='root',
        passwd='1234',
        host='127.0.0.1',
        db='isagagae',
        charset='utf8',
        port = 3305
    )
    # print(request.GET)
    cursor = user_rate.cursor(pymysql.cursors.DictCursor)
    # insert_data=[{'rate': request.GET['checked']}]
    insert_data=[{'user_id': '유저아이디9','user_pw': '유저패스워드',
                  'email': '유저이메일', 'type_id': '3', 'rate': request.GET['checked']}]
    insert_sql = "INSERT INTO `user` VALUES (%(user_id)s,%(user_pw)s,%(email)s,%(type_id)s, %(rate)s);"
    print(insert_sql)
    cursor.executemany(insert_sql, insert_data)
    user_rate.commit()


def savestar(request) :
    print(request.GET['checked'])
    rate = request.GET['checked']
    # user_rate_id = random.randint(1, 100000)
    # user_id = random.randint(1, 100000)
    # type_id = random.randint(1, 100000)
    # rate = request.GET['checked']
    # data = {'user_rate_id' : user_rate_id,
    #         'user_id' : user_id,
    #         'type_id' : type_id,
    #         'rate' : rate}
    to_db(request)
    print('완료한 별점', rate)
    return render(request, 'star/index.html')

# def to_db(request):
#     star_rate = pymysql.connect(
#         user='root',
#         passwd='1234',
#         host='127.0.0.1',
#         db='isagagae',
#         charset='utf8',
#         port = 3305
#     )
#
#     print("data " , request)
#
#     cursor = star_rate.cursor(pymysql.cursors.DictCursor)
#     insert_data=[{'user_rate_id': random.randint(1, 100000),'user_id': data['user_id'],
#                   'type_id': data['type_id'], 'rate':data['rate']}]
#     insert_sql = "INSERT INTO `user_rate` VALUES (%(user_rate_id)s,%(user_id)s,%(type_id)s, %(rate)s);"
#     cursor.executemany(insert_sql, insert_data)
#     star_rate.commit()







##### 원래 내 함수
# def savestar(request) :
#
#     user_input_star = int(request.GET['checked'])
#     to_db(user_input_star)
#     print('완료한 별점', user_input_star)
#     return HttpResponse(user_input_star)
#     # return redirect(reverse('index'))

