# nmap_automation
required files:<br/>
nmap_discovery.py<br/>
nmap_to_csv.py<br/>
parse-nmap.ps1<br/>

Install python3 to c:\python3 (to c:\ to avoid issues with potential spaces in directories.)<br/>
Download required files.<br/>
put all required files into a directory of your choice.<br/>
open CMD and cd to directory containing requried files.<br/>
run in CMD:   Python nmap_discovery.py<br/>

You will be asked:<br/>
`Enter an IP or subnet: (Example: 192.168.1.0/24 or 192.168.1.1-50):`<br/>
You can enter in CIDR or range. Examples: 192.168.1.0/24 or 192.168.1.1-100<br/>

`Enter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000):` <br/>
You can enter a range or use just "-". Examples: 1-1000 or -<br/>
Note that the code enteres the -p for this field already, do not enter it here.



    Please select the type of nmap scan you would like to run
          2) SYN ACK Scan (-sS -v)
          3) Scan UDP Ports (-sU -v)
          4) OS Discovery (-O)
          5) Custom 

    Would you like to review full report?
        1) Yes 
        2) No



You will get the following files created in the directory of nmap_discovery.py.
    
scan.csv<br/>
this is a basic csv of the scan details. It only shows the top OS guess, to get all OS guesses run the full report.
    
iplist.csv <br/>
this is a list of only active IP's. Can be used with other tools as a list.
    
outfile.xml <br/>
this is the main output from nmap. This can be used with ".\parse-nmap.ps1 outfile.xml" to read just the full report without rerunning the script. You can also import this to a database.
    
