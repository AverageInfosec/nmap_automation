# nmap_automation
required files:
nmap_discovery.py
nmap_to_csv.py
parse-nmap.ps1

Install python3 to c:\python3 (to c:\ to avoid issues with potential spaces in directories.)
Download required files.
put all required files into a directory of your choice.
open CMD and cd to directory containing requried files.
run in CMD:   Python nmap_discovery.py

You will be asked:
  Enter an IP or subnet: (Example: 192.168.1.0/24 or 192.168.1.1-50): 192.168.1.0/24

  Enter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000): 1-1000


  >Please select the type of nmap scan you would like to run
   >     2) SYN ACK Scan (-sS -v)
    >    3) Scan UDP Ports (-sU -v)
     >   4) OS Discovery (-O)
     >   5) Custom 
        
  Would you like to review full report?
      1) Yes 
      2) No
    
    
    
    
    You will get the following files created in the directory of nmap_discovery.py.
    
    scan.csv - this is a basic csv of the scan details. It only shows the top OS guess, to get all OS guesses run the full report.
    
    iplist.csv - this is a list of only active IP's. Can be used with other tools as a list.
    
    outfile.xml - this is the main output from nmap. This can be used with ".\parse-nmap.ps1 outfile.xml" to read just the full report without rerunning the script. You can also import this to a database.
    
