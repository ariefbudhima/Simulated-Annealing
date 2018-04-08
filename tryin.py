import decimal

# test = float(input('emosi = '))
# test1 = float(input('provokasi = '))

test=[97.00,36.00,63.00,82.00,71.00,79.00,55.00,57.00,40.00,57.00,77.00,68.00,60.00,82.00,40.00,80.00,60.00,50.00,100.00,11.00,58.00,68.00,64.00,57.00,77.00,98.00,91.00,50.00,95.00,27.00]
test1=[74.00,85.00,43.00,90.00,25.00,81.00,62.00,45.00,65.00,45.00,70.00,75.00,70.00,90.00,85.00,68.00,72.00,95.00,18.00,99.00,63.00,70.00,66.00,77.00,55.00,64.00,59.00,95.00,55.00,79.00]

for i in range(len(test)):
    # print test[i],test1[i]
    rendah1 = 0
    rendah2 = 0
    sedang1 = 0
    sedang2 = 0
    tinggi1 = 0
    tinggi2 = 0
    ya = 10
    tidak = 10

    if test[i] <= 25:
        rendah1 = 1

    elif test[i] < 50:
        rendah1 = (50 - test[i]) * 4 / 100
        sedang1 = (test[i] - 25) * 4 / 100

    elif test[i] < 75:
        tinggi1 = (test[i] - 50) * 4 / 100
        sedang1 = (75 - test[i]) * 4 / 100

    elif test[i] <= 100:
        tinggi1 = 1.0

    if test1[i] <= 25:
        rendah2 = 1.0

    elif test1[i] < 50:
        rendah2 = (50.0 - test1[i]) * 4 / 100
        sedang2 = (test1[i] - 25) * 4 / 100

    elif test1[i] < 75:
        tinggi2 = (test1[i] - 50) * 4 / 100
        sedang2 = (75 - test1[i]) * 4 / 100

    elif test1[i] <= 100:
        tinggi2 = 1.0

    # print "Emosi = 1"
    # print "rendah = ", rendah1
    # print "sedang = ", sedang1
    # print "tinggi = ", tinggi1
    # print
    # print "Provokasi"
    # print "rendah = ", rendah2
    # print "sedang = ", sedang2
    # print "tinggi = ", tinggi2
    # print

    if rendah1 > 0:
        if rendah2 > 0:
            if rendah1 < rendah2:
                tidak = rendah1
            else:
                tidak = rendah2
        if sedang2 > 0:
            if tidak > sedang2:
                tidak = sedang2
        if tinggi2 > 0:
            if tinggi2 < rendah1:
                ya = tinggi2
            else:
                ya = rendah1

    if sedang1 > 0:
        if rendah2 > 0:
            if sedang1 < rendah2:
                tidak = sedang1
            else:
                tidak = rendah2
        if sedang2 > 0:
            if tidak > sedang2:
                tidak = sedang2
        if tinggi2 > 0:
            if tinggi2 < sedang1:
                ya = tinggi2
            else:
                ya = sedang1

    if tinggi1 > 0:
        if rendah2 > 0:
            if tinggi1 < rendah2:
                tidak = tinggi1
            else:
                tidak = rendah2
        if sedang2 > 0:
            if sedang2 < tinggi1:
                ya = sedang2
            else:
                ya = tinggi1
        if tinggi2 > 0:
            if ya > tinggi2:
                ya = tinggi2

    if ya > 1:
        ya = 0
    if tidak > 1:
        tidak = 0

    pers = (tidak*100 + ya*50) / (tidak+ya)

    if (pers > 50):
        print i+1,'tidak'
    else:
        print i+1,'ya'