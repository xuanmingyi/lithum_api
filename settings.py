DATABASE_URI = 'mysql+pymysql://root:@localhost/zabbix'


try:
    from local_settings import *
except:
    pass