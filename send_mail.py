from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import configparser

def read_config(path,name):
    config = configparser.ConfigParser()
    config.read(path)
    config_dict = dict(config[name])
    type_dict = {"int":int,"float":float,"str":str}
    for key,value in config_dict.items():
        type_, value = value.split(",")
        config_dict[key] = type_dict[type_](value)
    return config_dict

def send_email(subject:str, body:str) -> bool:
    dic = read_config("./config.ini","gmail")
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(dic["adress"], dic["password"])

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = dic["adress"]
    msg['To'] = dic["to"]
    msg['Date'] = formatdate()

    smtpobj.send_message(msg)
    smtpobj.close()
    return True

if __name__ == "__main__":
    send_email("Execution completed","Execution completed")