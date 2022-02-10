penny = int(input("Введите число от 1 до 99: "))
# if (penny == 1 or penny == 21 or penny == 31 or penny == 41 or penny == 51 or penny == 61 or
#         penny == 71 or penny == 81 or penny == 91):
#     print("{0} копейка".format(penny))
# elif (penny == 2 or penny == 3 or penny == 4 or penny == 22 or penny == 23 or penny == 24 or penny == 32 or
#       penny == 33 or penny == 34 or penny == 52 or penny == 53 or penny == 54 or penny == 62 or
#       penny == 63 or penny == 64 or penny == 72 or penny == 73 or penny == 74 or penny == 82 or
#       penny == 83 or penny == 84 or penny == 92 or penny == 93 or penny == 94):
#     print("%d копейки" % penny)
# else:
#     print("%d копеек" % penny)
kop = penny
if 11 <= kop <= 14:
    print(penny, "копеек")
else:
    kop = kop % 10
    if kop == 1:
        print(penny, "копейка")
    elif 2 <= kop <= 4:
        print(penny, "копейки")
    else:
        print(penny, "копеек")
