i = 0
studentDict = dict()
list = []
list0 = []
count = 100
while i < 3:
    student_name = input("Enter student name and surname : ")       # Öğrencilerin bilgilerini giriyorum.
    student_mgrade = int(input("Ente student midterm grade : "))
    student_pgrade = int(input("Enter student project grade : "))
    student_fgrade = int(input("Enter student final grade : "))

    passing_grade = (student_mgrade * 0.3) + (student_pgrade * 0.3) + (student_fgrade * 0.4)
    studentDict[student_name] = round(passing_grade)       # Sözlük oluşturup içine bilgileri atıyorum.
    print("\n"+"************************************************************")
    i += 1
for keys in studentDict.keys():                            # Bu for döngüsünde keys değişkenini sözlüğümdeki anahtarlara sıra sıra atıyorum ve boş bir listeye değerlerini atıyorum.
    list.append(studentDict[keys])
list.sort(reverse = True)

while count >=0:                                           # Puanlara göre oluşturduğum listeyi isimlere göre olmasını istediğim içim m değişkenine bağlı bir while açıyorum 
    for keys in studentDict.keys():                        # Bu sayede hem aynı puanlı öğrenciler sorun çıkarmıcak.
        if studentDict[keys] == count:
            list0.append(keys)
    count = count - 1
print(list0)