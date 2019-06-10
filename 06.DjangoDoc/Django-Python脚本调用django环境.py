### 在Python脚本中调用Django环境:
if __name__ == '__main__':
	# 加载Django项目的配置信息
	import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
	# 到入Django,并启动Django项目
    import django
    django.setup()

    from app01 import models
    books = models.Book.objects.all()
    print(books)
