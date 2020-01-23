# nmap_automation
required files:<br/>
nmap_discovery.py<br/>
xml_to_csv.ps1<br/>
parse-nmap.ps1<br/>

Install python3 to c:\python3 (to c:\ to avoid issues with potential spaces in directories.)<br/>
Download required files.<br/>
put all required files into a directory of your choice.<br/>
open CMD and cd to directory containing requried files.<br/>
run in CMD: 

        Python nmap_discovery.py

You will be asked:<br/>
`Enter an IP or subnet: (Example: 192.168.1.0/24 or 192.168.1.1-50):`<br/>
You can enter in CIDR or range. Examples: 192.168.1.0/24 or 192.168.1.1-100<br/>

`Enter Ports to scan: (Example: enter just "-" for all ports, 21,22,80,443 or 1-1000):` <br/>
You can enter a range or use just "-" to scan all ports. Examples: 1-1000 or -<br/>
Note that the code has the -p for this field already, do not enter it here.<br/><br/>

Next you will be asked: <br/>


    Please select the type of nmap scan you would like to run
          1) Comprehensive Scan (-T4 -A -v)
          2) SYN ACK Scan (-sS -v)
          3) Scan UDP Ports (-sU -v)
          4) OS Discovery (-O)
          5) Custom 
And then finally you can choose to review the full report in CMD or just save the output to your directory. <br/>
      
      Would you like to review full report?
        1) Yes 
        2) No



You will get the following files created in the directory of nmap_discovery.py.
    
scan.csv<br/>
this is a csv of the scan details. If you run a comprehensive scan make sure you save it somewhere before you run any other scans as it will overwrite this file.
    
iplist.csv <br/>
this is a list of only active IP's. Can be used with other tools as a list to be called. This will continue to append and remove any duplicates based on the scans your perform. delete this file to start fresh.
    
outfile.xml <br/>
this is the main output from nmap. You can also import this to a database.<br/><br/><br/>

You may wish to review the full report after having performed your scans. <br/>
You can do this by opening powershell and cd to the directory with the required files and run: 

            .\parse-nmap.ps1 outfile.xml
