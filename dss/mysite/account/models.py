from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True, verbose_name='아이디')
    user_pw = models.CharField(max_length=50, verbose_name='비밀번호')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')

    # 테이블 생성 클래스
    class Meta:
        db_table = 'user_info'
