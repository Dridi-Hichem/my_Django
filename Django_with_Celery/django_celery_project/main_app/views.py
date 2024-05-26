from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from .tasks import test_func
from send_mail_app.tasks import send_mail_func

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=23, minute=24)
    task, created = PeriodicTask.objects.get_or_create(
        crontab=schedule,
        name="schedule_mail_task",
        task="send_mail_app.tasks.send_mail_func",
    )
    return HttpResponse("Mail Scheduled")
