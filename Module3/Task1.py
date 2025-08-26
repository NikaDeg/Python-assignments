length = float(input("Enter the length of the zander in centimeters: "))
missing_cm = 42 - length
if length < 42.0:
    print ("The zander does not meet the size limit.\nPlease release the fish back into the lake.")
    print (f"The fish was {missing_cm:.1f} centimeters below the size limit.")
if length >= 42.0:
    print ("The zander meets the size limit.")
