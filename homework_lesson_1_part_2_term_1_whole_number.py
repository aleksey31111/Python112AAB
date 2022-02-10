whole_number = int(input("Введите целое число: "))
if not (whole_number % 2):
    print("Число %d - четное" % whole_number)
elif (whole_number % 2):
    print("Число {0} нечетное".format(whole_number))
