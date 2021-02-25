from datetime import timedelta, datetime
import csv
from os import listdir
import glob
import pyttsx3
import pytz
import speech_recognition as sr

# = datetime.datetime.now().time()
#print(a.hour)
#print(a.minute)
#print(a.second)
#print(a)
#print(type(a.second))

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id) 
    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()
    
    
    
def get_audio():
    r = sr.Recognizer()
    
    while True:
        try: 
            with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""
                said = r.recognize_google(audio,language = "tr-TR") ##google api ile ne söylendiğini anlamlandırıyoruz. "tr-TR"
                print(said)
                break
        except Exception as e:
            print("Emir Bekliyor: ",str(e))
            
    return said.lower()  

def logMedicine():

    medicine = []
    period = []
    intakeTime = []


    speak("Lütfen ilaç adını belirtin:" )
    medicineToAppend = get_audio()
    medicine.append(medicineToAppend)
    speak("Lütfen ilacın saatlik olarak periyodunu belirtin: ")
    periodToAppend = int(get_audio())
    period.append(periodToAppend)
    print(type(period[0]))

    #intakeCheck = input("Bu ilacı bugün kullandıysanız en son saat kaçta kullandınız: (Kullanmadıysanız: n - saati saat-dakika olarak belirtin:)")
    speak("Lütfen bu ilacı bugün daha önce kullandıysanız kullanım saatinizi belirtin; ilacı kullanmadıysanız cevabınızı hayır olarak belirtiniz.")
    intakeCheck = get_audio()

    if intakeCheck == "hayır":
        speak("Lütfen ilacınızın ilk dozunu şimdi alın. Diğer dozlarınız için de, oluşturduğum kullanım planına göre size haber vereceğim!")

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
        speak("Kullanım planınızı oluşturuyorum, dozlarınız için size uygun saatlerde haber vereceğim!")

        dailyIntake = int(24 / period[-1])
        intakeTime.append(getHour(intakeCheck))
        intakeHour = getHour(intakeCheck).split(",")
        intakeHour = intakeHour[0]
        intakeMinute = getHour(intakeCheck).split(",")
        intakeMinute = intakeMinute[1]
            
        for i in range (0, dailyIntake - 1):
            hourAppend = int(intakeHour) + period[0] * (i + 1)

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

def getHour(check):

    for i in range(0, len(check)):
        
        if check[i] == ".":
            time = check.split(".")
            hour = int(time[0])
            minute = int(time[1])
            new_time = str(hour) + ',' + str(minute)
            return new_time

    for i in range(0, len(check)):
        
        if check[i] == " ":
            time = check.split(" ")
            hour = int(time[0])
            minute = int(time[1])
            new_time = str(hour) + ',' + str(minute)
            return new_time
    
    if len(check) == 3:
        hour = int(check[0])
        minute = int(check[1:3])
        new_time = str(hour) + ',' + str(minute)
        return new_time

    if len(check) == 4:
        hour = int(check[0:2])
        minute = int(check[2:4])
        new_time = str(hour) + ',' + str(minute)
        return new_time

    

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
                        speak(medicineName + " ilacını alma vaktiniz geldi!")
                    else:
                        pass
                        #print(check, row)
                        #print(str(row.strip("[]")))

#logMedicine()
#checkMedication()

            
    
