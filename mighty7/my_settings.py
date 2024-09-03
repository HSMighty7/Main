DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'TRAVEL', 
        'USER' : 'root', 
        'PASSWORD' : 'asd53014554!',
        'HOST': 'db.cxeaa4sem1o5.ap-northeast-2.rds.amazonaws.com', 
        'PORT': '3306',
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

SECRET_KEY = {
    'secret' : 'django-insecure-9#%$kd)a=8st2&3px35qmf=!$_0%$&8h1rm)$h&#v_&@rp^79h'
}