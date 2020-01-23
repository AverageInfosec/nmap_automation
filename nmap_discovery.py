#!c:/Python/python.exe
import sys
import os
from datetime import datetime
import time
import csv
import shutil


#Ask for user input and assign IP\subnet and port range.
print('<' + "-"  * 40 + '>')#style options
ip_range = '192.168.3.132' #str(input('\nEnter an IP or subnet: (Example: 192.168.1.0/24 or 192.168.1.1-50) '))
user_ports = '1-500' #str(input('\nEnter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000)'))
print("\nScanning IP " + ip_range + ". For ports " + user_ports + ".")

def run_nmap():
    #add banner containing time stamps for calculating time elapsed
    before = datetime.now()
    #nmap scan config
    nmap_scan = ("nmap " + ip_range + " -p" + user_ports + " " + nmap_arguments + " -oX outfile.xml")
    #convert xml to csv
    os.system( nmap_scan )
    os.system('exit' )
    #Finished time
    after = datetime.now()
    print("Time finished: "+ str(datetime.now().strftime('%m-%d-%Y %H:%M:%S')))
    print('<' + "-"  * 40 + '>')#style options
    #time elapsed during scan
    delta =  after-before
    print("Time elapsed: " + str(delta))
    print('<' + "-"  * 40 + '>')#style options

while True:
    scanops = input("""Please select the type of nmap scan you would like to run
        1) Comprehensive Scan (-T4 -A -v)
        2) SYN ACK Scan (-sS -v)
        3) Scan UDP Ports (-sU -v)
        4) OS Discovery (-O)
        5) Custom \n""")
    print("You have chosen: ", scanops)

    if scanops == '1':
            nmap_arguments = '-T4 -A -v'
            run_nmap()
            print(nmap_arguments)
            break
    elif scanops == '2':
            nmap_arguments = '-sS -v'
            run_nmap()
            break
    elif scanops == '3':
            nmap_arguments = '-sU -v'
            run_nmap()
            break
    elif scanops == '4':
            nmap_arguments = '-O'
            run_nmap()
            break
    elif scanops == '5':
            nmap_arguments = str(input('\nEnter nmap options: '))
            run_nmap()
            break
    else:
            print("Please enter a valid option")

os.system("powershell -NoProfile -ExecutionPolicy ByPass .\\xml_to_csv.ps1")
os.system('exit' )

#Make a copy of scan csv to create an IP list
shutil.copyfile('scan.csv', 'ip_temp_list.csv')


#remove duplicates from scan.csv
rows = csv.reader(open('scan.csv', 'r', newline=''))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open('scan.csv', 'w', newline=''))
writer.writerows(newrows)


#make a csv with just IP's
with open("ip_temp_list.csv","r") as source:
    rdr= csv.reader( source )
    next(rdr)
    next(rdr)
    with open("iplist.csv","w", newline='') as result:
        wtr= csv.writer( result )
        in_iter= ( (r[3],) for r in rdr )
        wtr.writerows( in_iter )

#remove temp csv file
os.remove("ip_temp_list.csv")
#os.remove("outfile.xml")


#remove duplicates from iplist.csv
rows = csv.reader(open('iplist.csv', 'r', newline=''))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open('iplist.csv', 'w', newline=''))
writer.writerows(newrows)
    
while True:
    review_report = input('''Would you like to review full report?
    1) Yes
    2) No
    ''')

    if review_report == '1':
        os.system("powershell -NoProfile -ExecutionPolicy ByPass .\\parse-nmap.ps1 outfile.xml ")
        os.system('exit' )
        break
    elif review_report == '2':
        print('Selected No')
        break
    else:
        print("Please enter a valid option")
