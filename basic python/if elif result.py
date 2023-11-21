Bangla1 = 70
Bangla2 = 60
English1 = 50
English2 = 60
General_Math = 80
Highermath = 60
P_Highermath = 22
Boilogy = 65
P_Boilogy = 23
Physics = 45
p_Physics = 24
Islamic_Religion =85
Social_Seience = 70
ICT = 75

Overall_Bangla = (Bangla1 + Bangla2) / 2

if(Overall_Bangla >= 33 and Overall_Bangla <= 39):
    print("Bangal: D")
elif(Overall_Bangla >= 40 and Overall_Bangla <= 49):
    print("Bangla: C")
elif(Overall_Bangla >= 50 and Overall_Bangla <= 59):
    print("Bangla: B")
elif(Overall_Bangla >= 60 and Overall_Bangla <= 69):
    print("Bangla: A-")
elif(Overall_Bangla >= 70 and Overall_Bangla <= 79):
    print("Bangla: A")
elif(Overall_Bangla >= 80 and Overall_Bangla <= 100):
    print("Bangla: A+")
elif(Overall_Bangla > 100):
    print("Invalid")
else:
    print("Bangla: Failed")



Overall_English = (English1 + English2) / 2

if(Overall_English >= 33 and Overall_English <= 39):
    print("English: D")
elif(Overall_English >= 40 and Overall_English <= 49):
    print("English: C")
elif(Overall_English >= 50 and Overall_English <= 59):
    print("English: B")
elif(Overall_English >= 60 and Overall_English <= 69):
    print("English: A-")
elif(Overall_English >= 70 and Overall_English <= 79):
    print("English: A")
elif(Overall_English >= 80 and Overall_English <= 100):
    print("English: A+")
elif(Overall_English > 100):
    print("Invalid")
else:
    print("English: Failed")




if(General_Math > 33 and General_Math <= 39):
    print("General Math: D")
elif(General_Math >= 40 and General_Math <= 49):
    print("General Math: C")
elif(General_Math >= 50 and General_Math <= 59):
    print("General Math: B")
elif(General_Math >= 60 and General_Math <= 69):
    print("General Math: A-")
elif(General_Math >= 70 and General_Math <= 79):
    print("General Math: A")
elif(General_Math >= 80 and General_Math <= 100):
    print("General Math: A+")
elif(General_Math > 100):
    print("Invalid")
else:
    print("General Math: Failed")




if(Highermath > 33 and Highermath <= 39):
    print("1.0")
elif(Highermath >= 40 and Highermath <= 49):
    print("2.0")
elif(Highermath >= 50 and Highermath <= 59):
    print("3.0")
elif(Highermath >= 60 and Highermath <= 69):
    print("3.5")
elif(Highermath >= 70 and Highermath <= 79):
    print("4.0")
elif(Highermath >= 80 and Highermath <= 100):
    print("5.0")
elif(Highermath > 100):
    print("Invalid")
else:
    print("Failed")



Overall_highermath = Highermath + P_Highermath



if(Overall_highermath > 33 and Overall_highermath <= 39):
    print("Highermath: D")
elif(Overall_highermath >= 40 and Overall_highermath <= 49):
    print("Highermath: C")
elif(Overall_highermath >= 50 and Overall_highermath <= 59):
    print("Highermath: B")
elif(Overall_highermath >= 60 and Overall_highermath <= 69):
    print("Highermath: A-")
elif(Overall_highermath >= 70 and Overall_highermath <= 79):
    print("Highermath: A")
elif(Overall_highermath >= 80 and Overall_highermath <= 100):
    print("Highermath: A+")
elif(Overall_highermath > 100):
    print("Invalid")
else:
    print("Highermath: Failed")



Overall_blilogy = Boilogy + P_Boilogy


if(Overall_blilogy > 33 and Overall_blilogy <= 39):
    print("D")
elif(Overall_blilogy >= 40 and Overall_blilogy <= 49):
    print("Boilogy: C")
elif(Overall_blilogy >= 50 and Overall_blilogy <= 59):
    print("Boilogy: B")
elif(Overall_blilogy >= 60 and Overall_blilogy <= 69):
    print("Boilogy: A-")
elif(Overall_blilogy >= 70 and Overall_blilogy <= 79):
    print("Boilogy: A")
elif(Overall_blilogy >= 80 and Overall_blilogy <= 100):
    print("Boilogy: A+")
elif(Overall_blilogy > 100):
    print("Invalid")
else:
    print("Boilogy: Failed")



Overall_pysics = Physics + p_Physics



if(Overall_pysics > 33 and Overall_pysics <= 39):
    print("Physics: D")
elif(Overall_pysics >= 40 and Overall_pysics <= 49):
    print("Physics: C")
elif(Overall_pysics >= 50 and Overall_pysics <= 59):
    print("Physics: B")
elif(Overall_pysics >= 60 and Overall_pysics <= 69):
    print("Physics: A-")
elif(Overall_pysics >= 70 and Overall_pysics <= 79):
    print("Physics: A")
elif(Overall_pysics >= 80 and Overall_pysics <= 100):
    print("Physics: A+")
elif(Overall_pysics > 100):
    print("Invalid")
else:
    print("Failed")





if(Islamic_Religion > 33 and Islamic_Religion <= 39):
    print("Islam: D")
elif(Islamic_Religion >= 40 and Islamic_Religion <= 49):
    print("Islam: C")
elif(Islamic_Religion >= 50 and Islamic_Religion <= 59):
    print("Islam: B")
elif(Islamic_Religion >= 60 and Islamic_Religion <= 69):
    print("Islam: A-")
elif(Islamic_Religion >= 70 and Islamic_Religion <= 79):
    print("Islam: A")
elif(Islamic_Religion >= 80 and Islamic_Religion <= 100):
    print("Islam: A+")
elif(Islamic_Religion > 100):
    print("Invalid")
else:
    print("Failed")





if(Social_Seience > 33 and Social_Seience <= 39):
    print("Seience: D")
elif(Social_Seience >= 40 and Social_Seience <= 49):
    print("Seience: C")
elif(Social_Seience >= 50 and Social_Seience <= 59):
    print("Seience: B")
elif(Social_Seience >= 60 and Social_Seience <= 69):
    print("Seience: A-")
elif(Social_Seience >= 70 and Social_Seience <= 79):
    print("Seience: A")
elif(Social_Seience >= 80 and Social_Seience <= 100):
    print("Seience: A+")
elif(Social_Seience > 100):
    print("Invalid")
else:
    print("Failed")





if(ICT > 33 and ICT <= 39):
    print("ICT: D")
elif(ICT >= 40 and ICT <= 49):
    print("ICT: C")
elif(ICT >= 50 and ICT <= 59):
    print("ICT: B")
elif(ICT >= 60 and ICT <= 69):
    print("ICT: A-")
elif(ICT >= 70 and ICT <= 79):
    print("ICT: A")
elif(ICT >= 80 and ICT <= 100):
    print("ICT: A+")
elif(ICT > 100):
    print("Invalid")
else:
    print("Failed")


Total_Mark = Bangla1 + Bangla2 + English1 + English2 + General_Math + Highermath + P_Highermath + Boilogy + P_Boilogy +Physics + p_Physics + Islamic_Religion + Social_Seience + ICT
total_mark = f"Total Mark: {Total_Mark}"
print(total_mark)

gpa = (Overall_Bangla + Overall_English + General_Math + Overall_highermath + Overall_blilogy + Overall_pysics + Islamic_Religion + ICT) / 8

if(gpa > 33 and gpa <= 39):
    print("GPA: 1.0")
elif(gpa >= 40 and gpa <= 49):
    print("GPA: 2.0")
elif(gpa >= 50 and gpa <= 59):
    print("GPA: 3.0")
elif(gpa >= 60 and gpa <= 69):
    print("GPA: 3.5")
elif(gpa >= 70 and gpa <= 79):
    print("GPA: 4.0")
elif(gpa >= 80 and gpa <= 100):
    print("GPA: 5.0")
elif(gpa > 100):
    print("Invalid")
else:
    print("Failed")