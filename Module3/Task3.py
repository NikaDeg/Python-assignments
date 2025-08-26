gender = str(input("Enter biological gender (male/female): "))
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gender.lower() != "male" and gender.lower() != "female":
    print ("Invalid gender.")
elif gender.lower() == "male" and hemoglobin > 167 or gender.lower() == "female" and hemoglobin > 155:
    print ("Your hemoglobin is high.")
elif gender.lower() == "male" and 134 > hemoglobin or gender.lower() == "female" and 117 > hemoglobin :
    print ("Your hemoglobin is low.")
else: print ("Your hemoglobin is normal.")
