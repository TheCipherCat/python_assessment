import re
import pathlib

def parselog():
    log_file = pathlib.Path("/home/student/assessment/catlog.txt")
    log_content = log_file.read_text()
    auth_port = re.findall(r"port\s(\d{1,5})\s", log_content, re.IGNORECASE) #From auth log
    win_port = re.findall(r"Client Port:\s(\d{1,5})\s", log_content, re.IGNORECASE) #Microsoft-Windows-Security-Auditing log
    fwall_sport = re.findall(r's_port:\"(\d{1,5})\";', log_content, re.IGNORECASE) #Firewall log s_port
    fwall_service = re.findall(r'service:\"(\d{1,5})\";', log_content, re.IGNORECASE) #Firewall log service port number
    print(auth_port,win_port, fwall_sport,fwall_service)

parselog()
