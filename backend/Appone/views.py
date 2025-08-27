from django.http import JsonResponse
from django.core.cache import cache
from .models import ExampleModel
import datetime 

def grade(score, breakpoints=[60, 70, 80, 90], grades=['F', 'D', 'C', 'B', 'A']):
    return grades[score]


def home(request):
    data = cache.get("examplemodeldata")

    if not data:
        print("⚡ 從資料庫讀取 ExampleModel")
        queryset = ExampleModel.objects.all()
        data = list(queryset.values())  # Django 會自動序列化 datetime

        # 存快取（直接存 Python 物件，django-redis 幫你 pickle）
        cache.set("example_data", data, timeout=20)
    else:
        print(f"從 Redis 快取讀取 ExampleModel: {datetime.datetime.now()}", )

    return JsonResponse({"results": data}, safe=False)