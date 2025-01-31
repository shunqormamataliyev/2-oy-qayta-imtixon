
from datetime import datetime
from itertools import count
from os import write
from symtable import Class

###1-misol
# from datetime import datetime, timedelta
# def sana_year(date_sana: str):
#     try:
#         date_mal = datetime.strptime(date_str, '%Y-%m-%d')
#
# # Test
# print(sana_year('2025-01-01'))
# print(sana_year('Salom'))

###2-misol
# class User:
#     def __init__(self, name, rol,):
#         self.name = name
#         self.rol = rol
#
# class Exam:
#     def __init__(self, owner, baho):
#         self.owner = owner
#         self.__baho = baho
#
#     def baholar(self, admin, natija):
#         if admin.rol == "O'qituvchi":
#             self.__baho = natija
#             return self.__baho
#         else:
#             return "error"
#
# Shunqor = User("Shunqor","Talaba")
# Shoxjahon = User("Shoxjahon","O'qituvchi")
# baho = Exam(Shoxjahon,4)
# print(baho.baholar(Shoxjahon, 5))

###3-misol
import requests

###4-misol


###5-misol
# def setter(x: str):
#     n = x.replace(' ','')
#     r = n.replace('-','')
#     p = r.replace(',', '')
#     return p
#
# print(setter("""AI-powered spreadsheets help you and your team manage, visualize and analyze data.”"""))

###6-misol
# def toq_son(son: int):
#     if son % 2 == 1:
#         return True
#     else:
#         return False
# print(toq_son(3))

###7-misol
# def rekursiya_summ(List: list[int]):
#     if len(List) == 0:
#         return 0
#     return List[0] + rekursiya_summ(List[1:])
#
# numbers_list = [1, 2, 3, 4, 5]
# result = rekursiya_summ(numbers_list)
# print(f"List elementlar yig'indisi: {result}")


###8-misol
# import random
# x = random.randint(1,10)
# print("Kompyuter 1 dan 10 gacha son o'yladi Uni topishga harakat qiling!")
# while True:
#     y = int(input('1 dan 10 gacha son kiriting: '))
#     if x == y:
#         print(f"Siz yutdingiz va bu son {x} edi")
#         break
#     else:
#         print(" Topolmadingiz iltimos qayta kiriting:")

###9-misol
# import random
# print("Kompyuter 1 dan 10 gacha son o'yladi Uni topishga harakat qiling!")
# y = int(input('1 dan 10 gacha son kiriting: '))
# t = []
# while True:
#     x = random.randint(1, 10)
#     t.append(x)
#     if x == y:
#         print(f"Kompyuter siz kiritgan sonni topdi va bu son  {y} edi\nUrunishlar soni: {len(t)}")
#         break




