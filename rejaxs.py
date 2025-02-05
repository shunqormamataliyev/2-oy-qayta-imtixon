"""1. Matnni faqatgina raqam va harflardan (a-z, A-Z, 0-9) iborat
ekanligini tekshiruvchi dastur tuzing"""
from requests.packages import imported_mod

# import  re
# pattern = re.compile("^[a-zA-Z0-9]+$")
# print(pattern.search("2e323bdsdGG"))

"""2. Matnni boshlanishi a harfi va undan keyin 0 ta yoki undan
kop marta b harfi yozilishi bilan tekshiring
Misol :
matn = “abb” >> True ohiri a + bb bilan tugayapti
matn = “ac” >> False ohiri a + c bu a dan keyin b kelishi kerak
matn = “a” >> True ohirida a bilan tugayapti b harfi 0 ta"""
# import re
# pattern = re.compile("^ab*$")
# print(pattern.match("ab"))

"""3. Matn ichida a va undan keyin b harfidan bitta yoki undan
kop marta qatnashganligi bo’yicha tekshiring"""
# import re
# pattern = re.compile("a+b+")
# print(pattern.search("tyvghabb"))

"""4. Matn ichida a va undan keyin b harfidan 0 ta yoki 1 marta
qatnashganligi bo’yicha tekshiring"""
# import re
# pattern = re.compile("a+b?")
# print(pattern.search("tyvghab"))

"""5. Matn ichida a va undan keyin b harfidan 3 marta
qatnashganligi bo’yicha tekshiring"""
# import re
# pattern = re.compile("a+b{3}")
# print(pattern.search("tyvghabbbcv"))

"""6. Matn ichida a va undan keyin b harfidan 2 yo’ki 3 marta
qatnashganligi bo’yicha tekshiring"""
# import re
# pattern = re.compile("a+b{2,3}")
# print(pattern.search("tyvghabcv"))

"""7. Matn ichida bitta Katta harf va undan keyin va matnning
ohiri kichkina harflar bilan tugaganligi bo’yicha tekshiring"""
# import re
# pattern = re.compile("[A-Z]{1}\+[a-z]$") b       #ishlash kerak
# print(pattern.search("tYvghabcv"))

"""8. email uchun regex yozing"""
# import re
# pattern = re.compile("^[a-zA-Z0-9]+[@gmail.com$]")
# print(pattern.match("yvghabcv3@gmail.com"))         #ishlash jerak

"""9. Telefon raqam uchun regex yozing"""
# import re
# pattern = re.compile("^\+998\d{9}$")                 #hatolik bor
# print(pattern.search("+998937179764"))

"""10. Sizga patterns = [‘fox’, ‘dog’, ‘horse’] nomli ro’yhat va
text = “The quick brown fox jumps over the lazy dog.”
nomli string berilgan sizning vazifangiz shu ro’yhatdagi
har bir elementni shu textda borligiga tekshiring agar bor
bo’lsa “Matched !” so’zini aks holda “Not Matched”
so’zini chiqaring"""
import re
patterns = ['fox', 'dog', 'horse']
text = "The quick brown fox jumps over the lazy dog."
for pattern in patterns:
    if re.search(pattern,text):
        print("Matched!")
    else:
        print("No Matched ")




