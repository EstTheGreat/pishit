import os
import glob
import datetime
import time


def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Type Date dd/mm/yy hour:minute : ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%d/%m/%y %H:%M")
            isValid=True
        except:
            print "Date not valid, try again.\n"
    return d

'''
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '10*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
   
#Above code is used to read temp and access sensor.
#Users choice starts around here

    x = read_temp()
    print "Current temperature:", x
    '''


while True: #checks that input is the desired one
    input_var = raw_input("1. Insert how long the car should heat for.\n2. Insert a time by which the car should be heated.\nInsert 1 or 2 for your choice: ")
    if (input_var == '1' or input_var == '2'):
        break
    else: print"Insert 1 or 2 to select your choice."

if (input_var == '1'): #duration of heating process as suggested by Miro
    print("How long would you like to heat the car for?")
    hours_heated = raw_input("Hours: ") 
    minutes_heated = raw_input("Minutes: ")

    while True : 
        yesorno1 = raw_input("Would you like to start heating now? y/n  ")

        if(yesorno1 == 'y' or yesorno1 == 'n'):
            break
        else: 
            print("Insert y for yes and n for no")

    if (yesorno1 == 'y'): #heating starts right away
        heatingtime = int(hours_heated)*3600 + int(minutes_heated)*60
        print "The car would heat for", heatingtime , "seconds"
        
        #missing relay commands would go here, instead of the print statement above
        
        pass

    if (yesorno1 == 'n'): #heating is delayed 
       
        while True:
            yesorno2 = raw_input("1. Insert date\n2. Insert timer\nInsert 1 or 2 for your choice: ")
            if (input_var == '1' or input_var == '2'):
                break
            else: print"Insert 1 or 2 to select your choice."

        if(yesorno2 == '2'): #heating is delayed by an amout of time
            print("\nIn how long would you like to start heating?")
            days_waiting = raw_input("Days: ")
            hours_waiting = raw_input("Hours: ")
            minutes_waiting = raw_input("Minutes: ")
            wait_before_heating = int(days_waiting)*86400 + int(hours_waiting)*3600 + int(minutes_waiting)*60
            print "The raspberry now knows it would need to wait ",wait_before_heating,"secs before starting the heating process"
            pass 

        if(yesorno2 == '1'): #heating is delayed till a specified date
            userdate = ObtainDate() #fetches the date with the ObtainDate function

            from datetime import datetime   
            today = datetime.now() #fetches the current date
            print ("The raspberry now knows it would need to wait "+(userdate-today).seconds)+"seconds before starting the heating process." 
                                                                    #Above here ^ we subtract user give date by todays date
                                                                    #this way we get how many seconds the pi would need to wait
            pass

    pass    

if (input_var == '2'): #here we fetch a date by which the raspberry will have the car heated (line 52s IF)

    usergivendate2 = ObtainDate()
    from datetime import datetime  
    today2 = datetime.now()
    waittimesecs = (usergivendate2-today).seconds 

    heatingtime2 = 1
        #calculate the time needed to heat the car here!!  use x = current temperature and heatingtime2 = properly calculate formula
'''
        if (x < -15):
         heatingtime2 = 9000
        
 
        elif(x>-15 and x < -5):
            heatingtime2 = 4500
        
        elif(x > -5 and x < 5):
            heatingtime2 = 2700
        
        elif(x>5 and x<12):
            heatingtime2 = 1200

        else: 
            print "The car does not need to be heated "
'''
print("Calcualted time needed for heating is: "+heatingtime2+"seconds") #relay commands here...?
pass    

        