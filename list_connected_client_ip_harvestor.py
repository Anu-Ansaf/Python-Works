import pyshark
capture = pyshark.LiveCapture(interface='Wi-Fi',display_filter="tcp")
capture.sniff(timeout=20)

top_10_nmap_port = [7,9,13,21,22,23,25,26,37,53,79,80,81,88,106,110,111,113,119,135,139,143,144,179,199,389,427,443,444,445,465,513515,543,544,548,554,587,631,646,873,990,993,995,1025,1026,1027,1028,1029,1110,1433,1720,1723,1755,1900,2000,2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000,6001,6646,7070,8000,8008,8009,8080,8081,8443,8888,9100,9999,10000,32768,49152,49157]

target = str(input("Enter Target IP address:"))

counter = 0
for x in range(len(capture)):
    
    for j in top_10_nmap_port:
        port = str(j)
        
        try:
            if capture[x]['ip'].dst == '192.168.43.46' and capture[x]['ip'].src == target :
                ip = capture[x]['ip'].src
                if (capture[x]['TCP'].dstport == port ):
                    counter = counter + 1
        except KeyError or IndexError :
            pass
  
if  counter > 90:
    print(capture[x]['ip'].src + " Scanned Top 100 PORTS ")

print(capture[0]["TCP"].flags)