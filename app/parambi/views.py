from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models.objects import RegistroHeader, RegistroDetalhe


@csrf_exempt
def truncate_tables(request):
    RegistroDetalhe.objects.all().delete()
    RegistroHeader.objects.all().delete()

    return JsonResponse({'status': 'ok'}, safe=False)