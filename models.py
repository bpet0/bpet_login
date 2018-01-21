from sqlalchemy import Column, Integer, String, SmallInteger, Float, DateTime
from database import Base
import json
from _datetime import datetime

class User(Base):
    __tablename__ = "t_user"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_name = Column('user_name', String(128), unique=True, default='')
    nick_name = Column('nick_name', String(128), default='')
    phone_num = Column('phone_num', String(32), unique=True, default='')
    email = Column('email', String(200), unique=True, default='')
    password = Column('password', String(128), default='')
    gender = Column('gender', SmallInteger, default=-1)
    birthday = Column('birthday', DateTime, default=datetime.now())
    longitude = Column('longitude', Float, default=0)
    lattitude = Column('lattitude', Float, default=0)
    address = Column('address', String(128), default='')
    default_pet = Column('default_pet', Integer, default=-1)
    head_portrait = Column('head_portrait', String(256), default='')

    '''
    def __init__(self, user_name=None, nick_name=None, phone_num=None, email=None,
                 password=None, gender=None, birthday=None, longitude=None,
                 lattitude=None,address=None,default_pet=None,head_protrait=None):
        self.user_name = user_name
        self.nick_name = nick_name
        self.phone_num = phone_num
        self.email = email
        self.password = password
        self.gender = gender
        self.birthday = birthday
        self.longitude = longitude
        self.lattitude = lattitude
        self.address = address
        self.default_pet = default_pet
        self.head_portrait = head_protrait
    '''

    def __init__(self, params={}):
        if 'user_name' in params:
            self.user_name = params['user_name']
        if 'nick_name' in params:
            self.nick_name = params['nick_name']
        if 'phone_num' in params:
            self.phone_num = params['phone_num']
        if 'email' in params:
            self.email = params['email']
        if 'password' in params:
            self.password = params['password']
        if 'gender' in params:
            self.gender = params['gender']
        if 'birthday' in params:
            self.birthday = params['birthday']
        if 'longitude' in params:
            self.longitude = params['longitude']
        if 'lattitude' in params:
            self.lattitude = params['lattitude']
        if 'address' in params:
            self.address = params['address']
        if 'default_pet' in params:
            self.default_pet = params['default_pet']
        if 'head_portrait' in params:
            self.head_portrait = params['head_protrait']

    def __repr__(self):
        return "<User %r>" % self.user_name

    def __str__(self):
        return json.dumps({'id':self.id,
                           'user_name':self.user_name,
                           'nick_name':self.nick_name,
                           'phone_num':self.phone_num,
                           'email':self.email,
                           'password':self.password,
                           'gender':self.gender,
                           'birthday':self.birthday.strftime('%Y-%m-%d'),
                           'longtitude':self.longitude,
                           'lattitude':self.lattitude,
                           'address':self.address,
                           'default_pet':self.default_pet,
                           'head_portraint':self.head_portrait,
                           })
