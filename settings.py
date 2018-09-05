DATABASE_URI = 'mysql+pymysql://root:@172.16.29.32/zabbix'


try:
    from local_settings import *
except:
    pass