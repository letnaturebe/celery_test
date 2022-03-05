from typing import List

import requests
from celery import shared_task
from celery.result import AsyncResult
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@shared_task()
def task(emails: List[str]) -> None:
    for _ in emails:
        requests.post('https://httpbin.org/delay/1')


@csrf_exempt
def send_emails(request):
    emails: List[str] = request.POST.get('emails')
    task_id = task.delay(['1.naver.com', '2.naver.com', '3.naver.com'])
    return JsonResponse({'task_id': task_id.id})


def task_status(request):
    task_id = request.GET.get('task_id')

    if task_id:
        task: AsyncResult = AsyncResult(task_id)
        if task.state == 'FAILURE':
            error = str(task.result)
            response = {
                'state': task.state,
                'error': error,
            }
        else:
            response = {
                'state': task.state,
            }
        return JsonResponse(response)