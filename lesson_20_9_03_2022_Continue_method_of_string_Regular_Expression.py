###### LESSON 20 19.03.2022
##### Continue Method Of String ####
#### rfind - Get 1 - 3 Arguments. -1 - Not FOUND
# s = "hello, WORLD! I am learning Python."
# print(s.rfind("l"))  # Index LAST ELEMENT.
# print(s.rfind("al"))  # Index LAST ELEMENT.

### Task 2: ###
# str = " Send unlimited free texts and make WiFi calls from a free phone number. Download the free app"
# fin = "f"
# for x in str:
#     if fin.find(x) != -1:
#         if len(fin.find(x)) == 1:
#             print(fin.find(x))
#         if len(fin.find(x)) == 2:
#             print(fin.find(x))

## NOT Full
# for i in s:
#     if i == "f":
#         print(s.index(i))
#         print(s.rindex(i))
#         break

## Not All True
# c = 'send unlimited fee texsts and make WiFi calls from a free phone number'
#
#
# def func(x):
#     for i in x:
#         if x.count('f') > 2:
#             print(x.find('f'), x.rfind('f'))
#         if x.count('f') == 1:
#             print(x.find('f'))
#         else:
#             break
#
#
# func(c)


# c = 'send unlimited fee texsts and make WiFi calls from a free phone number'
#
#
# def func(x):
#     if x.count('f') > 2:
#         print(x.find('f'), x.rfind('f'))
#     if x.count('f') == 1:
#         print(x.find('f'))
#
#
# func(c)

#
# c = 'send unlimited fee texsts and make WiFi calls from a free phone number'
#
#
#
# if s.count('f') > 2:
#     print(s.find('f'), s.rfind('f'))
# elif c.count('f') == 1:
#     print(s.find('f'))

### tASK 2: ###
# c = 'send unlimited fee texsts and make WiFi calls from a free phone number'
# if s.count('f') ==2:

# ## True ##
# s = "I am learning Python. hello, WORLD!"
# start = s.find("e")
# end = s.rfind("e")
# print(start, end)
# s1 = s[0:start]
# s2 = s[end + 1:]
# s_new = s1 + s2
# print(s_new)
#
#
# ## True ##
# c = 'I am learning Python. hello, World!'
# c = c[:c.find('h')] + c[c.rfind('h') + 1:]
# print(c)

###### CONTINUE LESSON ######
# s = "hello, WORLD! I am learning Python."
# print(s.endswith("lo", 0, 5))  # End Str with BOOLERN
# print(s.startswith("I am", 14))  # Start Str with BOOLERN
#
# print('abs123'.isalnum)  # String Contant NUM, STR.  TRUE
# print("".isalnum())  # FALSE
#
#
# print("ABCabc".isalpha())  # Str Contain ONLY LETTER   TRUE
# print("ABC123".isalpha())  # FALSE
#
# print('123'.isdigit())  # Only NAMBER  TRUE
# print('123abc'.isdigit())  # Only NAMBER  FALSE
#
# print("abc".isidentifier())  # VALID IDENTIFIER
# print("1abc".isidentifier())  # NOT VALID IDENTIFIER
# print("%abc".isidentifier())  # NOT VALID IDENTIFIER
#
# print('abc'.islower())  # lower registr NUM and LETTER TRUE
# print('Abc'.islower())  # FALSE
# print('abc$123'.islower())  # TRUE
#
# print(" \t \n".isspase())  # String Contain SPACE CHARACTER.
# print(" a ".isspace())  # False
#
# print("The Apple".istitle())  # Every WORLD 1 Letter Capitalise  TRUE
# print("The apple".istitle())  # FALSE

# ISUPPER()
# ISUPPER()


# ##### FORMAT method #####
# print("py".center(10, "-"))
# print("py".center(3,"#"))
# print("py".center(9, "-"))
#
#
# #### Delete SPICE #####
# print('      py'.lstrip())
# print('py         '.rstrip())
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(";$."))
#
# print('https://www.python.org'.lstrip('/:pths').rstrip("org."))
#
# print("     py     ".strip())
# print("https://www.python.org/".strip("/org.w:pths"))

# s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(s.replace("Nython", "Python"))  # Change old on New
# print(s.replace("N", "P"))
# print(s.replace("Nython", "Python", 2))  # Change old on New

# ##### Transform Type Of DATA #####
# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# #### print("..".join([1, 2]))  # ERROR
# print(":".join('Hello'))
#
# print("Срока разделенная пробелами".split())
# print("Срока разделенная пробелами".split(" "))
# print("www.puthon.org".split("."))
# print("www.puthon.org".split(".", 1))
# print("www.puthon.org.ru".split(".", 1))
#
# a = input("--> ").split()
# print(a)

# ### Task 3: ###
# # a = input("Enter FIO: ").split()
#
# a = 【"Bashkirov" "Aleksey" "Aleksandrovich"】
# # a = input('-> ').split()
# print(a[0], a[1][:1]+'.', a[2][:1]+'.')
#
#
# # a = input('-> ').split()
# print(a[0], a[1][0]+'.', a[2][0]+'.')


# print("www.puthon.org".rsplit("."))  #
# print("www.puthon.org".rsplit(".", 1))


### Task 4: ###
# str1 = " В строке заменить пробелы символом"
# str1.replase

# str1 = " В строке заменить пробелы символом"
# s = '*'.join((input('Введите строку: ').split()))
# s = '*'.join(str1.split()))

################ REGULAR EXPRESSIONS #####################################
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# reg = 'я'
# print(s.find(reg))
# print(reg in s)

# import re
# s = "Я ищу совпадения в 2021 году. И я их обязательно найду. 4546"
# print(s)
# reg = 'я'
# # reg1 = 'совпадения'
# # reg2 = "Я ищу"
# reg3 = "."
# reg4 = "\\."
# reg5 = r'\.'
# print(re.findall(reg, s))  # Return LIST Contain All math
# print(re.findall('12', s))
#
# print(re.search(reg, s))  # Return 1 Found Math and Finit Work
# print(re.search(reg, s).span())  # From start to End
# print(re.search(reg1, s).span())    # From start to End
# print(re.search(reg1, s).start())
# print(re.search(reg1, s).end())
# print(re.search(reg1, s).group())
#
# print(re.match(reg1, s))
# print(re.match(reg2, s))
#
# print(re.split(reg, s))
# print(re.split(reg3, s))
# print(re.split(reg4, s))
# print(re.split(reg5, s))
#
# print(re.sub(reg, "!", s))
# print(re.sub(reg, "!", s, 1))

# import re
# s = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. 4546"
# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg = r'2021'
# reg1 = r'[201]'
# reg2 = r'[0-9]'
# reg3 = r'[12][0-9][0-9][0-9]'
# reg4 = r'[а-я]'
# reg5 = r'[а-яё]'
# reg6 = r'[Аа-яё]'
# print(re.findall(reg, s))  #[2021
# print(re.findall(reg1, s))
# print(re.findall(reg2, s))
# # From 1900 - 2999
# print(re.findall(reg3, s))
# print(re.findall(reg4, s))
# print(re.findall(reg4, s1))
# print(re.findall(reg5, s1))
# print(re.findall(reg6, s1))


# s= "Еда, беду, победа"
# reg7 = '[Ее]д[ау]'
# print(re.findall(reg7, s1))
#
# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg6 = r'[Аа-яё.]'
# print(re.findall(reg6, s1))
# s2 = "Ели[-ели]."
# reg7 = r'[А-Яа-яё.-]'
#
# reg8 = r'[А-Яа-яё.\[\]-]'
# print(re.findall(reg8, s2))
#
# reg9 = r'[^ 0-9]'
# reg10 = r'[1-2]'

# ### Task 5 ###
# str5 = " 12345 1234515:671222"
# reg11 = "[12][0-9]:[0-9][0-9]"
# print(re.findall(reg11, str5))


# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg = r'\.'

###### ABREVIATURE #######
# s1 = "Я ищу совпадения в 2021 году. 1987 И я их обязательно найду. Найду в два счета."
# reg12 = r'\D'  # eny NAM
# reg13 = r'\w'  # Nam, Lett
# reg14 = r'\s'  # Space
# reg15 = r'\D'  # NOT eny NAM
# reg16 = r'\w'  # NOT Nam, Lett
# reg17 = r'\s'  # NOT Space
# print(re.findall(reg12, s1))
# ##### \A \B \Z ##### \a \b \z #####