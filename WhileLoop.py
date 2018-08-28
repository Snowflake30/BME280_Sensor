# Author: Lacie Brown 
# Date	:
# Discp	: This program will run the BME280_Sensor in a while loop. Then it
# 	: will send this data to a website to display the sensor readings 
# 	: along with the drone's data. The program also does a write to
#       : file function, the file directory is below. 
# File  : home/pi/BMESensorProject
# File  : SensorData.txt (Text file with run data, saved to local drive) 


import BME280_Sensor as bme280
import time
from time import sleep
import os
import sys
import datetime
import csv
import gps 
    
false = KeyboardInterrupt

# This earses previous data within the txt file, remove "w" if previous run data
# is needed and replace with "a+" 
f = open("SensorData.txt", "w").close()

# Chip Data is displayed first and only once. 
print('Chip Data')
bme280.DisplayChipData()
print('\n')

# Display the date and time for clean data collection and save to txt file as well
time = time.time()
dattime = datetime.datetime.fromtimestamp(time).strftime('Today is: ''%Y-%m-%d \nThe time is: ''%H:%M:%S')
f = open("SensorData.txt", "a+")
f.write(str(dattime)+"\n")
print(dattime)

#Get users input to begin displaying sensor readings
user_input = input("\nPress enter to begin and CTRL C to quit \n")

# Output Sensor and GPS readings to screen in a loop until CTRL C is pressed
try:
    while(True):
        # Take Sensor Readings and Display
        data = bme280.SensorDataDict()
        temperatureC = data["TempC"]
        temperatureF = data["TempF"]
        pressure = data["Pressure"]
        humidity = data["Humidity"]
        print("Temperature = ", temperatureC, "C")
        print("Temperature = ", temperatureF, "F")
        print("Pressure = ", pressure, "hPa")
        print("Humidity = ", humidity, "%")
        print("\n")
        sleep(2)
        # Take GPS Readings and Display
        gps_data = gps.GPS_Data()
        Latitude = gps_data["latitude"]
        Longitude = gps_data["longitude"]
        Latitude_dir = gps_data["latitude_direction"]
        Longitude_dir = gps_data["longitude_direction"]
        print("Latitude = ", Latitude, Latitude_dir)
        print("Longitude = ", Longitude, Longitude_direction)
        print("\n")
        sleep(2)

        # Save Info to text file
        f = open("SensorData.txt", "a+")
        f.write(str(data)+"\n")
        
# When CNTR C is pressed, finish by saving to file
except false:
    print("\nInterrupted,  closing out")
    # Write the final reading displayed to the txt file
    f.write(str(data)+"\n")
    f.close() # final check to see if the txt file is closed 

# Exit the program safely 
sys.exit()


