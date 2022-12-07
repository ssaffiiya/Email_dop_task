
import re
with open('кондуит 2022 - Преподаватели и ассистенты.tsv', 'r+',encoding="utf-8") as f:
    text=f.read()
    email=re.sub(r'[a-zA-Z0-9._-]*@hse.ru',"Pr1v@cY REstorED",text)
    email_end = re.sub(r'[a-zA-Z0-9._-]*@edu.hse.ru',"Pr1v@cY REstorED",email)

