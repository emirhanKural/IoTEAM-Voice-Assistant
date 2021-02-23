from datetime import timedelta, datetime
import csv
from os import listdir
import glob
# = datetime.datetime.now().time()
#print(a.hour)
#print(a.minute)
#print(a.second)
#print(a)
#print(type(a.second))

def logMedicine():

    medicine = []
    period = []
    intakeTime = []


    medicineToAppend = input("Lütfen ilaç adı giriniz:" )
    medicine.append(medicineToAppend)
    periodToAppend =  int(input("Lütfen ilacın saatlik olarak periyodunu giriniz: "))
    period.append(periodToAppend)
    print(type(period[0]))

    intakeCheck = input("Bu ilacı bugün kullandıysanız en son saat kaçta kullandınız: (Kullanmadıysanız: n - saati saat-dakika olarak belirtin:)")

    if intakeCheck == "n":

        b = datetime.now().time()
        intakeTime.append(str(b.hour) + ',' + str(b.minute))
        dailyIntake = int(24 / period[-1])
        print(dailyIntake)

        for i in range (0, dailyIntake - 1):

            intakeToAppend = datetime.now() + timedelta(hours=period[0] * (i + 1))
            intakeToAppend = str(intakeToAppend.hour) + ',' + str(intakeToAppend.minute)
            intakeTime.append(intakeToAppend)

        print(intakeTime)

    else:

        dailyIntake = int(24 / period[-1])
            #intakeTime.append(intakeCheck)

        for i in range(0, dailyIntake - 1):

                #currentTime = datetime.now().time()
                #currentHour = currentTime.hour
                #currentMinute = currentTime.minute

            if len(intakeCheck) == 4:
                intakeHour = int(intakeCheck[0])
                if intakeCheck[2] == 0:
                    intakeMinute = intakeCheck[-1]
                else:
                    intakeMinute = intakeCheck[2:4]
            else:
                intakeHour = int(intakeCheck[0:2])
                if intakeCheck[2] == 0:
                    intakeMinute = intakeCheck[-1]
                else:
                    intakeMinute = intakeCheck[3:5]

        intakeTime.append(str(intakeHour) + ','+ str(intakeMinute))
            
        for i in range (0, dailyIntake - 1):
            hourAppend = intakeHour + period[0] * (i + 1)

            if hourAppend == 24:
                hourAppend = "00"

            if int(hourAppend) > 24:
                hourAppend = int(hourAppend) - 24

            intakeToAppend = str(hourAppend) + ','+ str(intakeMinute)
            intakeTime.append(intakeToAppend)

        print(medicine)
        print(intakeTime)

    f = open(medicine[0]+'.csv', 'w')

    with f:
        writer = csv.writer(f)
        for row in intakeTime:
            writer.writerow([row])
    medicine = []
    intakeTime = []
    period = []

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

def checkMedication():
    while True:   
        a = datetime.now().time()
        a_hour = a.hour
        a_minute = a.minute
        check = str(a_hour)+','+str(a_minute)
        print(check)
        #logMedicine()
        filenames = find_csv_filenames(r"C:\Users\Lenovo\Desktop\ehe\Gereksiz\SAMSUNG IOT\Proje\ehe")

        for i in range(0, len(filenames)):
            print("Okunan dosya:", filenames[i])

            with open(filenames[i], "rt", encoding='ascii') as infile:
                read = csv.reader(infile)
                for row in read:
                    row = ''.join(row)
                    if check == row:
                        medicineName = filenames[i].split(".")
                        medicineName = medicineName[0]
                        print(medicineName, "ilacını alma vaktiniz geldi!")
                    else:
                        #print(check, row)
                        #print(str(row.strip("[]")))
                        
logMedicine()
checkMedication()
            
        
    







    
