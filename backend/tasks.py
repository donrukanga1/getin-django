from celery import task
import random
import datetime

from backend.models import PregnantGirl, PresetMessage, AntenatalVist
from backend.sms_handler import utils



@task()
def send_preset_sms():
    for girl in PregnantGirl.objects.all():
        preset_message = random.choice(PresetMessage.objects.all())

        if girl.contact_number[0] == '0':
            phone_number = '256' + girl.contact_number[1:]
        else:
            phone_number = girl.contact_number

            sms = utils.gateway.sendMessage(phone_number, preset_message.text)

        return sms

def send_vht_reminder_sms(vht, girl):
    msg = "%s has an ANC appointment in two days. She can be reached on %s." % girl.name, girl.contact_number

    if vht.phone_number[0] == '0':
        phone_number = '256' + vht.phone_number[1:]
    else:
        phone_number = vht.phone_number

        sms = utils.gateway.sendMessage(phone_number, msg)
    return sms

def send_powerholder_reminder_sms(girl):
    msg = "%s has an ANC appointment in two days. Don't forget." % girl.name

    if girl.contact_number[0] == '0':
        phone_number = '256' + girl.contact_number[1:]
    else:
        phone_number = girl.contact_number

        sms = utils.gateway.sendMessage(phone_number, msg)
    return sms

@task()
def send_reminder_sms():
    for appointment in AntenatalVist.objects.all():
        if datetime.today() + datetime.timedelta(days=2) == appointment.date:
            send_powerholder_reminder_sms(appointment.girl)
            send_vht_reminder_sms(appointment.girl.mapped_by, appointment.girl)
