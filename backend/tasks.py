from celery import task
import random

from backend.models import PregnantGirl, PresetMessage
from backend.sms_handler.utils import send_sms



@task()
def send_sms():
    for girl in PregnantGirl.objects.all():
        preset_message = random.choice(PresetMessage.objects.all())
        sms = send_sms(girl.contact_number, preset_message.text)

        return sms