# 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

User_log = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

time1 = User_log[7:9]
time2 = User_log[10:12]
time3 = User_log[13:15]
summa = int(time1) + int(time2) + int(time3)
print(summa)
