#!c:/Python/python.exe
import sys
import os
from datetime import datetime
import time
import csv
import shutil



#style options
print('<' + "-"  * 40 + '>')
#Ask for user input and assign IP\subnet.
ip_range = str(input('\nEnter an IP or subnet: (Example: 192.168.1.0/24 or 192.168.1.1-50. Leave blank to perform a custom scan): '))


#Function to perform an nmap scan
def run_nmap():
    #time stamp for calculating time elapsed
    before = datetime.now()
    #nmap scan config
    nmap_scan = ("nmap " + ip_range + " " + user_ports + " " + nmap_arguments + " -oX outfile.xml")
    os.system( nmap_scan )
    os.system('exit' )
    #Finished time
    after = datetime.now()
    print("Time finished: "+ str(datetime.now().strftime('%m-%d-%Y %H:%M:%S')))
    #style options
    print('<' + "-"  * 40 + '>')
    #time elapsed during scan
    delta =  after-before
    print("Time elapsed: " + str(delta))
    #style options
    print('<' + "-"  * 40 + '>')

#ask the user what type of nmap scan they wish to perform, and adds arugments to do the specific types
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
            user_ports = str(" ")
            run_nmap()
            print(nmap_arguments)
            break
    elif scanops == '2':
            nmap_arguments = '-sS -v'
            user_ports = str(" ")
            run_nmap()
            break
    elif scanops == '3':
            nmap_arguments = '-sU -v'
            user_ports = str(" -p" +input('\nEnter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000): '))
            run_nmap()
            break
    elif scanops == '4':
            nmap_arguments = '-O'
            user_ports = str(" ")
            run_nmap()
            break
    elif scanops == '5':
            user_ports = str(" -p" +input('\nEnter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000): '))
            nmap_arguments = str(input('\nEnter nmap options: '))
            run_nmap()
            break
    else:
            print("Please enter a valid option")
#Create a CSV from the XML nmap created
os.system("powershell -NoProfile -ExecutionPolicy ByPass .\\xml_to_csv.ps1")
os.system('exit' )

#Make a copy of scan csv to create an IPlist
shutil.copyfile('scan.csv', 'ip_temp_list.csv')


#make a csv with namp scan details
with open("scan.csv","r") as source:
    rdr= csv.reader( source )
    next(rdr)
    with open("scan_report.csv","a", newline='') as result:
        wtr= csv.writer( result )
        in_iter= ( (r[0],r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9],) for r in rdr )
        wtr.writerows( in_iter )

#remove duplicates from scan.csv
rows = csv.reader(open('scan_report.csv', 'r', newline=''))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open('scan_report.csv', 'w', newline=''))
writer.writerows(newrows)       


#make a csv with just IP's
with open("ip_temp_list.csv","r") as source:
    rdr= csv.reader( source )
    next(rdr)
    next(rdr)
    with open("iplist.csv","a", newline='') as result:
        wtr= csv.writer( result )
        in_iter= ( (r[3],) for r in rdr )
        wtr.writerows( in_iter )

#remove temp csv files
os.remove("ip_temp_list.csv")
os.remove("scan.csv")


#remove duplicates from iplist.csv
rows = csv.reader(open('iplist.csv', 'r', newline=''))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open('iplist.csv', 'w', newline=''))
writer.writerows(newrows)

#Ask user if they wish to view full report in the CMD window
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
