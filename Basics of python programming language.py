#                    Mening ismim Sharofiddin Allaberdiev 
# Bugundan boshlab men sizlar bilan python dasturlash tili uchun asos bo'lib
# hizmat qiladigan vazifalari kodlar orqali darsni boshlayman.  
# Darsimiz maqsadi nafaqat dasturlash asoslarini balki bir vaqtning o'zida tur
# li xil muammolarga yechim bo'ladigan dasturlar yozishni o'rganishdir. 
# Bu dasturlash asosini Python dasturi orqali ko'rib chiqsakda, bu oladigan 
# bilim va ko'nikmalaringiz umumiydir.
# Bizning maqsadimiz bu kurs orqali sizni dasturlash olamiga tez va samarali
# yo'l bilan olib kirishdir. Bu darslar hayotida umuman biror dasturlash tili
# yoki python orqali kodlar yozmagan tinglovchilar uchun ham juda foydali bo'l
# adi deb umid qilamiz. Bu dasturlash kurslarini bitiruvchi tinglovchilar 
# kelajakda dasturlashning murakkab va tor yo'nalishlarida yoki umuman dasturl
# ashning boshqa til..ga ham oson va yengillik bilan o'ta oladi deb ishonamiz.
#  Ho'sh nima uchun Python. u o'rgaish uchun oson, qulay va bu dastur asosida
# yozilgan kodlar ko'p qirrali bo'ladi. Ya'ni bu dasturlash tili turini o'rgan
# ish bilan faqatgina bitta yo'nalishda emas, turlicha yo'nalishlarda ish faol
# iyatini olib borishingiz mumkin bo'ladi. misol uchun pyhton tili Web-dastur,
# o'yinlar yaratish, ma'lumotlar bazasi va ilmi bilan ishlash, Sun'iy intelek
# da ham keng qo'llaniladi. Bundan tashqari bugungi kunda bu dasturlash tilida
# ishlovchi mutaxssislarga talab kundan kunga ortib bormoqda. buni indeed.com
# mehnat saytida kuzatish mumkin. Bu juda keng qamrovli universal tildir. 
# python da yozilgan ko'dlar turli platforma va operatsiyon tizimlarda ishlaydi
# Yuqoridagi omillarni hisobga olgan holatda bizni kursimiz python ga asoslarndi

        #01 ANACONDA platformasidan foydalanamiz. uning uchun browser qidiruv 
 # tizimidan download ANACONDA deb qidirsak bo'ladi .com saytidan olsak bo'ladi
 # Agarda kimdadir ustanovka qilish qiyin kechsa repl.it saytidan foydalanishimiz
 # mumkin birinchi dasturimizni yozishga kirishamiz buning uchun sizda Anaconda
 # spyder, kite yordamchilarini ishga tushiramiz. Spyder dasturi ichida asosan
# matn muharriri va kosnoldan foydalanamiz.  

# Biz Spyderda Kite orqali avtocomplate ni yoqmoqchi bo'lsak ctrl + space ni
# bir marta bosib qo'yishimiz mumkin.

        #02 Birinchi dasturimiz 
# print("Hello world")

# endi 
# 7+8
# deb yozib ko'rdik ammo konsolda natija yo'q, bu amal bajarildimi yoki yo'qmi?
# Ha, albatta bajarildi biroq biz natijasini so'rmadik. biz buni bilish uchun
# print(7+8)
# va shu orqali javobini ko'rishimiz mumkin bo'ladi. Bu bizni birinchi dastur
# imiz edi. 
# Buni spyder dan boshqa joylarda ham tekshirib ko'rishimiz mumkin.

# Vazifa matn muharriri va konsolda matematik amallarni bajarib  
# javoblarini tekshirib ko'ring


        #03 PRINT(), SINTEKS VA ARIFMETIK AMALLAR
# Izoh = print() bu funksiyadir. 

# print("Assalom alaykum")

# print("Odamiy ersang demagil odamiy \nonikim yo'q halq g'amidin g'ami")

# print(100/4)

# print(15//4)

# print(5*2)

# print(5**2)

# print(5**5)

# print("to'qqizning kvadrati", 9**2, "ga teng")

# print('3x3=',3*3)

ism = input("Sizning to'liq ismingiz nima: ")
yosh = input("Sizning yoshingiz nechida: ")
print("uning to'liq ismi " + ism + " va uning yoshi " + yosh + "da")




        #04 O'zgaruvchilar. O'zgaruvchi ma'lumotlar zamirida biz o'zimizga 
# kerakli ma'lumotlarni dasturga kiritib borishimiz va ish jarayonida ularga 
#o'zgartirishlar kiritishimiz mumkin bo'ladi
# Tasavvur qiling bir quticha bor va uni ichiga kerakli ma'lumotlar solindi.
# Quti ustiga nom yozdingiz. keyingi galda bunga murojaat qilib oson topishga.
# Example
#ism = "Abdulloh"
#yosh = 25

#print(ism)
#print(yosh)

# Demak bu yerda biz ism yoki yosh deb nomlangan o'zgaruvchilarimizga qiymat
# berganimiz va bu bilan ma'lumotlarga qisqa murojaat qilib konsulga chiqarish
# mummkin bo'ladi.
# Biz ma'lumotlarni konsolda ham o'zgartirib ko'rishimiz mumkin. 
# buni biz variable explorer orqali ko'rishimiz mumkin.
   
# a = 5
# b = 4
# c = (a+b)**2
# print(c)

# Demak o'zgaruvchilarga ifoda shaklida topshiqiriqlar ham berishimiz mumkin.
# shuni ko'rib chiqdik.
# python.sariq.dev da o'zgaruvchilarga mos qoidalar ko'rsatib o'tilgan.

# konsolga help() undan keyin keywords desak ishlatilmasligi lozim bo'lgan
# o'zgaruvchi nomlarini ko'rsatadi. bundan quit so'zi orqali chiqib ketamiz.
# misol uchun for = 5 deb o'zgaruvchi yarata olmaymiz, sababi bu so'z 
# Python uchun maxsus command word hisoblanadi.





    # 05 Matn bilan ishlash. Unicode-table.com sayti orqali 
    # emojilarni use qilamiz
 
# p = 'enojini tanlab copy qilib qo'ying'

# ism = 'Alisher'
# familiya = 'Navoiy'
# print(ism + ' ' + familiya)

# Bu yerda ya'na boshqacha shakli mavjud. buni f-string usuli bilan ham
# jamlasak bo'ladi

# ism = 'Alisher'
# familiya = 'Navoiy'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = 'James'
# familiya = 'Bond'
# print(f"Salom mening ismim {familiya} {ism} {familiya}")

# print("Hello \tworld")
# print('Hello world')
# print("Hello \nworld")

    # string metodlari bu pythonda o'zida belgilab olingan amallardir

# ism = 'James'
# familiya = 'Bond'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# bu holatda faqat string matnimiz harflari kattalashadi. ma'lumotlar 
# esa o'zgarmaydi. .upper() , .lower()  , title() , .capitalize()
 
# ism = 'James'
# familiya = 'Bond'
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.lower()
# print(ism_sharif)

# meva = "           olma            "
# print('men ' + meva.lstrip() + 'ni yaxshi ko\'raman')


# meva = "           olma            "
# print('men' + meva.rstrip() + 'ni yaxshi ko\'raman')


# meva = "           olma            "
# print('men ' + meva.strip() + 'ni yaxshi ko\'raman')

# bu usuldan qidirsh tizimida foydalaniladi. bunda bo'shliq qolib ketgan
# bo'lsada so'zni tez topib olish imkoni bo'ladi

    # input fuksiyasi bu foydalanavchidan ma'lumot olish

# ism = input("ismingiz nima?")
# print("Salom, " + ism)

# Endi \n dan foydalanamib ko'ramiz 

# ism = input("ismingiz nima?\n>>>")
# print("Salom, " + ism.title())

# E'tibor bering bu yerda title metoddan bilan doimiy katta harf ga erishdik




    # 06 Sonlar Integer, floating point number, Demak butun dunyo dasturchili
    # gida kelishib olinganki 5.5 nuqta bilan ajratiladi vergul bilan emas.
    # int=(),   float(),   str()     
# bu o'zgaruvchilarni turini tekshirish uchun type() klasidan foydlansa bo'lad

# a = 10
# b = 6.5
# print(type(a))

# aholi_soni = 7_456_456_666
# print("Aholi soni: ", aholi_soni)

# Demak tagida beradigan chiziqlarimiz ekranda chiqarish uchun ta'siri yo'q

# x, y, z = 10, 4.5, 20
# print(y)

# d = 100/2
# print(type(d))

# d = bo'luv kasrli amal bo'lgani uchun uni float tipiga ta'luqli deb topadi

# Agarda 100//2 desak unda uni integer deb topadi

# d = 100//2
# print(type(d))

# radius = 20
# PI = 3.14159
# diametr = 2*radius
# print("aylana uzunligi=", PI*diametr)


# ism = "Jobir"
# yosh = 36
# yosh = str(yosh)
# xabar = ism + " " + yosh + " yoshda"
# print(xabar)

# Odatda bunday yechim berish noto'g'ri chunki yosh soni biz uchun mavhumga
# aylandi.

# ism = "Jobir"
# yosh = 36
# xabar = ism + " " + str(yosh) + " yoshda"
# print(xabar)

# t_yil = int(input("tug'ilgan yilingizni kiriting: "))
# yosh = 2021 - t_yil
# print("siz", yosh, "yoshda ekansiz")

# a = int("10")
# b = float("10")
# temp = str(36.6)

# Bu holatda matn bo'lgan "10" integer ga aylandi. b esa float ya'ni butun
# qismi bo'lgan songa aylandi. tempda esa son edi str bilan matn bo'ldi.





    # 07 Lists (ro'yxatlar). Bitta o'zgaruvchiga ko'plab ma'lumotlar yuklashni
    # ko'rib chiqamiz

# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik'] #mstnli ro'yhat
# narhlar = [344, 69, 565, -356, -45.6, 35.9]   # turli sonli ro'yhat'
# sonlar = ['bir', 'uch', 45, 58]   # sonlar va matnlar aralash ro'yhat
# ismlar = [] # bo'sh ro'yhat

#print(sonlar[-3].upper())
#print(narhlar[0] + narhlar[1]) 

#Endi elementlar tartibini o'zgatirishni ko'rib chiqamiz

# narhlar[0] = '565'
# #print(narhlar)

# sonlar[-1] = 'besh'
# #print(sonlar)


#         # .append() list ga yangi malumotni qo'shish buyrugi
# mevalar.append('banan')
# mevalar.append('tarvuz')

# mevalar.insert(5, 'gilos')
# print(mevalar)


# cars = []
# cars.append("Nexia")
# cars.append("Tracker")
# cars.append("Malibu")
# # print(cars)

# del cars[0]
# # print(cars)

# cars.insert(0, "Nexia 3")
# # print(cars)

# cars.remove("Malibu")
# print(cars)



#   .pop  methodi bilan ma'lumotlarni sug'urib olish mumkin bo'ladi
# bozorlik = ['go\'sht', 'un', 'piyoz']
# mahsulot = bozorlik.pop(1)
# print("Men sotib olgan mahsulot: ", mahsulot)
# print("sotib olinmagan mahsulotlar: ", bozorlik)





# 08 Lists (ro'yxatlar bilan ishlash). o'zgarmas ro'yhatlar (Tuples)
# Tartiblash    

# cars = ['bmw', 'mercedes benz', 'volvo', 'tesla', 'audi']
# print(cars)
# cars.sort()
# print(cars)

# Bu yerda biz buni tartibga olishni ko'rib chiqdik.
# E'tibor bering agarda biz list da elementini katta harflar bilan boshlasak
# unda birinchi o'ringa shu elementni qo'yadi. EXAMPLE;

# cars = ['bmw', 'Mercedes benz', 'volvo', 'tesla', 'audi']
# cars.sort()
# print(cars)

# Shu tufayli biz dastlab .upper(), lower(), title(), capitalise() yordamida
# tartibga keltirib keyin .sort() metodidan foydalanish maqsadga muvofiq bo'la

# cars = ['bmw', 'Mercedes benz', 'volvo', 'tesla', 'audi']
# print(sorted(cars, reverse=True))
# # bu reverse buyrug'i bilan biz uni teskari tartibda yozilishiga erishamiz.

# sonlar = [12, 45, 88, -10, -3, 45]
# print(sorted(sonlar))

# sonlar = [12, 45, 88, -10, -3, 45]
# print(sorted(sonlar, reverse=True))

# nechta so'zlar mavjudligini aniqlash uchun len metodidan foydalanamiz
# print(len(sonlar))

# Biz buni sonini element sifatida ishlatmoqchi bo'lganimizda zarur bo'ladi
# uni ishlatish uchun biz uzunlik degan o'zgaruvchiga tenglab olishimiz mumkin
# uzunlik = (len(sonlar))
# print(uzunlik)


# sonlar = [12, 45, 88, -10, -3, 45]
# sonlar = list(range(0, 10))
# print(sonlar)
# # Bu yerda biz list ichiga 0 dan 9 gacha bo'lgan raqamlarni joylashtirdik

# toq_sonlar = list(range(1, 20, 2))
# print(toq_sonlar)


# juft_sonlar = list(range(0, 20, 2))
# print(juft_sonlar)

# sanoq10lik = list(range(0, 110, 10))
# print(sanoq10lik)

# Maximal yoki min. qiymat chiqarish uchun quyidagi max metodidan foydalanamiz
# max_qiymat = max(sanoq10lik)
# print(max_qiymat)

# min_qiymat = min(sanoq10lik)
# print(min_qiymat)

# Agarda yig'indini topish kerak bo'lsa sum metodidan foydalanamiz

# print(sum(sanoq10lik))


# cars = ['bmw', 'mercedes benz', 'volvo', 'tesla', 'audi']
# print(cars[:3])
# # Bu yerda biz o'rtada qaysi qiymatlar kerak bo'lsa shu orqali ko'rib chiqamiz
# # va o'rganamiz

# cars = ['bmw', 'mercedes benz', 'volvo', 'tesla', 'audi']
# print(cars[1:3])

# my_cars = cars
# print(cars)

# my_cars.remove('volvo')
# print(my_cars)

# # [:] - belgisi copy qilib olib faqatgina shu matnga o'zgartirish kiritish 
# # mumkinligini anglatadi
# my_cars = cars[:]
# my_cars.remove('bmw')
# print(my_cars)
# print(cars)



#   Tuple o'zgarmas ro'yhat yaratish uchun ishlatiladi, 
# toys = ('bus', 'car', 'bear', 'snake')
# toys[0] = 'car'

#print(toys[0:3]) 
# print(toys) 

# TypeError: 'tuple' object does not support item assignment deydi sababi 
# bu o'zgarmas ro'yhat uchun ishlatiladi

# toys = list(toys)
# toys.append('bus')
# # print(toys)

# toys = tuple(toys)
# print(toys)




    # 09 for Tsikl bilan tanishish va ishlash
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim' ]
# print('Salom', mehmonlar[0])    
# print('Salom', mehmonlar[1:3])  


# for hamma in mehmonlar:
    # print('Salom', hamma)      


# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim' ]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorgi oshga taklif qil")
#     print("Hurmat bilan, Palonchievlar oilasi\n")

# ENDI SONLARNI KETMA KETLIKDA Kvadratga oshirishni ko'rib chiqamiz
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# Bu orqali 7 soni uchun 10 gacha ko'paytirish jadvali qilib ko'ramiz


# sonlar = list(range(1,11))
# # print(sonlar)
# for son in sonlar:
#     print(f"{7} x {son} = {7*son}")


# ism = 'Richard'
# familiya = 'Odongo'
# ism_sharif = f"{familiya}  ...  {ism}"
# print(ism_sharif)


# Agarda range ichiga dastlabki sonni ko'rsatmasak, u taqdirda 0 dan boshlaydi
# bu sonlarni ketma ketlikda ikkiga bo'lib ko'ramiz
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{2/son}")

# sonlar = list(range(11))
# print(sonlar)


# sonlar = list(range(11))
# for son in sonlar:
#     print(son)


# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []  # bo'sh ro'yhat
# print("5 ta eng yaqin do'stingiz kim? ")
# for n in range(5):
#     dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting: "))
# print(dostlar)



# 10 If va Else shartlari va tarmoqlanish
# Biz shu vaqtgacha e'tibor bergan bo'lsangiz ketma ket qatorma qator 
# bajariladigan kodlarni ko'rib o'tdik, bu chiziqli dastur deb ataladi. 
# Ammo dasturlar odatda bunday ishlamaydi, tassavur qiling siz biror bir o'yin
# o'ynayabsiz siz chapga yursangiz boshqa funksiya bajariladi yoki aksincha 
# chapga yursangiz boshqa bir funksiya bajariladi.yoki ijtimoiy dasturlar turk
# umiga kiruvchi facebook, instagram, tiktokdan foydalanganingizda qaysidir 
#funksiyaga kirish uchun topshiriq berganingizda u shu amalga qarab harakatlan
# bazi qismlari topshiriqga binoan bajarilmay o'tib ketishi mumkin bu 
# tarmoqlanishga kiradi. Buning uchun biz if operatoridan foydalanamiz. 


# avtolar = ['bmw', 'audi', 'kia', 'hyundai']
# for avto in avtolar:
#     print(avto.capitalize())

# Bu yerda agar biz 'bmw' so'zini kattalashtirmoqchi bo'lsak. bu bizga faqat 
# bosh harflarini kattalashtirib berganini ko'rishimiz mumkin. Agar biz so'zni
# katta harflarda yozmoqchi bo'lsak unga alohida buyruq so'zini berish mum. 
# NEGADIR AVTOLAR KODI MENDA KONSOLDA ISHLAB KODLAR QISMIDA ISHLAMADI

    
# avtolar = ['bmw', 'audi', 'kia', 'hyundai']

# for avto in avtolar: # ... avtolar ichida har bir avto uchun
#     if avto == 'bmw': # ... agar avto 'bmw' ga teng bo'lsa
#         print(avto.upper()) # ... avto nomini katta harflarda yoz
#     else:                       # aks holda ...
#         print(avto.title()) #... avt nomini faqat birinchi harfini kattada



# Konsolda bazi tekshiruv ishini olib boramiz. misol uchun 
# print(avto)  desak hyundai yozuviga teng deb ko'rsatmoqda. 
# avto == 'bmw' ga tengmi deb yozsak Out[32]: False degan ma'lumot beradi bu
# esa avto == 'hyundai' yozganimizda Out[33]: True degan ishorani beradi.
# agarda shu narsalarni katta va kichik matnda tekshirib ko'rsak kichik va kat
# ta matnli so'zlar bir biriga teng emasligini ko'rishimiz mumkin. Ehtiyot b.k
# == teng so'rog'i hisoblanadi, != teng emas so'rog'i hisoblanadi



# ism = input('ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"uzr, {ism.title()} biz Alini kutyabmiz.")
# else:
#     print("Salom, Ali")


# ism = input('ismingiz nima?\n>>>')
# if ism.lower() != 'sharofiddin': #..bu yerda .lower metodi yozuvni kichik 
#                     # qilib tekshirib ko'ryabdi.
#     print(f"uzr {ism.title()}, biz Sharofiddin ismli insonni kutyabmiz.")
# else:
#     print("Salom, xush kelibsiz Sharofiddin")

# javob = float(input("12x6 nechiga teng?\n="))
# if javob != 72:
#     print('javob xato!')
# else:
#     print('javob to\'g\'ri')


# Endi katta yoki teng >= operatoridan foydalanishni ko'rib chiqamiz

# yosh = int(input("Sizning yoshingiz nechida?\n>>>"))
# if yosh >= 18:
#     print('Xush kelibsiz, Siz bu xizmatdan foydalanishingiz mumkin!')
# else:
#     print('Sizning bu xizmatdan foydalanishingiz taqiqlanadi!')

# login = input("yangi login tanlang: ")
# if len(login) <= 5:
#     print("login 5 harfdan uzun bo'lishi shart")
    
# yil = int(input("Tug'ulgan yilingizni kiriting: ")) 
# if 2021-yil < 18:
#     print(f"Sizning yoshingiz {2021-yil} da ekan. siz uchun mumkin emas")
#     print("Sizning kirishingiz qat'iyan taqiqlanadi!")
# else:
#     print("Xush kelibsiz! iltimos, endi quyidagi savolnomaga javoblar bering")

# Biz kodlarni qisqa va tushunarli qilib yozishga erishishimiz zarur bo'ladi.
# Quyida ko'radigan ko'dimizni qisqa shaklda bayon etishimiz mumkin.
# ya'ni bir qatorda shart va uni print badalini yozishimiz mumkin.

# yosh = int(input("yoshingiz nechida? \n>>>"))
# if yosh > 65:   print("Ehtiyot bo'ling, Sizda COVID-19 ni yuqtirish riski yuqori ekan") 

# x, y = 40, 50
# print("x>y") if x>y else print("x<y")


# x = float(input("X ning qiymatini kiriting: >>> "))
# y = float(input("Y ning qiymatini kiriting: >>> "))
# print("x>y") if x>y else print("x<y")


        # 11 If, Elif, Else shartlari. Demak biz if va else bog'lamasi orqali
#  faqat 1ta shartni tekshirib ko'ra olamiz. 
# Endilikda tasavvur qilamiz bir nechta shartlar bor, va ularni tekshirishimiz
# kerak, va har bir shart natijasiga ko'ra u yoki bu qiymatni chiqarishimiz 
# kerak
# Misol uchun hayvonat bog'iga kirmoqchisiz, narxlar 3 xil toifalangan bo'lsin
# yoshlarga, o'rta yoshlilarga, qariyalarga. misol ishlaymiz

# yosh = int(input("Yoshingiz nechida? \n>>>"))
# if yosh <=4:
#     print("4 yoshgacha kirish bepul")
# elif yosh <=12:
#     print("Sizga kirish 5 000 so'm")
# elif yosh <=30:
#     print("Sizga kirish tekin")
# else: 
#     print("Sizga kirish 10 000 so'm")

# Endi buni boshqa qulay ifodada aks ettirish mumkinligini ko'rishimiz mumkin

# yosh = int(input("Yoshingiz nechida? \n>>>"))
# if yosh <=4:
#     narh = 0
# elif yosh <=12:
#     narh = 5000
# elif yosh <=23:
#     narh = 8500
# else: 
#     narh = 12000
# print(f"sizga kirish {narh} so'm ")


# Bizda ya'na boshqacha holat, ya'ni biz bir nechta boshqa shartlarni
# tekshirishimizga to'g'ri keladi. buning uchun biz OR yoki AND operatorlardan
# foydalanamiz. Buning uchun misollar ko'ramiz.

# kun = input("Bugun nima kun? >>> ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' :
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')



# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("havo harorati qanday? >>> "))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Mazza qilib cho'milish rejasini tuzish mumkin")
# elif kun.lower() == "yakshanba" and harorat < 30:
#     print("Uyda dam olganing ma'qul")
# else:
#     print("Cho'milish rejasini unut, ishga borishing kerak")

# bu holatda ko'rib o'tganimizdek if va and operatorlari to'g'ri bo'lgan, 
# bajarilgan holatida yuqoridagi print amallari bajariladi.



#   Endi BOOLEAN mantiqiy ma'lumotlar turi haqida suhbatlashamiz
# Tasavvur qiling restarantda mijoz taomlar sotib oldi, choy yoki salat oldi
# uni qanday hisoblaymiz

# narh = int(input("narhi qancha: "))
# choy = True
# salat = False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
#     print(f"jami {narh} so'm")
    

# Endi ko'p tomonlama tekshirish uchun kod yozamiz. Buning uchun if operatori 
# bilan alohida alohida tekshirib chiqamiz

taom_narh = 15000
choy = True
salat = False
non = False

print("+ Mijoz taom oldi.")
if choy:   #..agar choy olsa
    print("+ Mijoz choy oldi.")
    taom_narh = taom_narh + 2500
    
if salat:   #..agar salat olsa
    print("+ Mijoz salat oldi.")
    taom_narh = taom_narh + 5000
else:
    print("- Mijoz salat olmadi.")
    taom_narh = taom_narh
    
if non:
    print("+ Mijoz non oldi.")
    taom_narh = taom_narh + 2500
    
    print(f"  jami {taom_narh} so'm")

# # Bu yerda hamma shartlar tekshirildi



# taom_narh = 15000
# choy = 0
# salat = 1
# non = 1

# print("+ Mijoz taom oldi.")
# if choy:   #..agar choy olsa
#     print("+ Mijoz choy oldi.")
#     taom_narh = taom_narh + 2500
    
# if salat:   #..agar salat olsa
#     print("+ Mijoz salat oldi.")
#     taom_narh = taom_narh + 5000
    
# if non:
#     print("+ Mijoz non oldi.")
#     taom_narh = taom_narh + 2500
    
#     print(f"  jami {taom_narh} so'm")



# Endi IN operatorida ishlash amallarini ko'rib chiqamiz. Ma'lum bir matnni 
# ro'yhat ichida bor yoki yo'qligni tekshirishimiz mumkin 

# menu = ["osh", "qozon kabob", "manti", "norin", "somsa"]
# print('manti' in menu)

# Demak ma'lumot bor ekan True qiymati chiqdi. Endi 
# Keling, endi foydalanuvchi xohlagan ovqat bizda mavjudmi yo'qmi tekshirib
# ko'ramiz

# menu = ["osh", "qozon kabob", "manti", "norin", "somsa"]

# ovqat = input("nima ovqat yeyishni istaysiz?>>> ")
# if ovqat.lower() in menu:
#     print("buyurtma qabul qilindi.")
# else:
#     print("Afsuski bunday ovqat bizda mavjud emas")


# Endi NOT IN operatori bilan tanishamiz

# menu = ["qozon kabob", "norin", "somsa"]
# print("osh" not in menu)
# print('somsa' not in menu)


# Endi buyurtmachi bir qancha jihozlar ro'yhatini so'raydi, biz esa tekshirib
# beramiz

# menu = ["osh", "qozon kabob", "manti", "norin", "somsa"]
# buyurtmalar = ["kabob", "qozon kabob", "somsa"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
# konsolda ishladi


# buyurtmalar = []

# if buyurtmalar:
#     print(f"ro'yhatda {len(buyurtmalar)} ta taom bor")
# else: 
#     print("ro'yxat bo'sh")
# konsolda ishladi

# Mus.l topshi.lar asosida berilgan vazifalarni o'zingizga tahlil qilib oling


















