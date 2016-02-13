import re
from backend.sms_handler import AfricasTalkingGateway
from getin.settings import SMS_GATEWAY_USERNAME, SMS_GATEWAY_API_KEY

gateway = AfricasTalkingGateway(SMS_GATEWAY_USERNAME, SMS_GATEWAY_API_KEY)

def send_sms(number, message):
    if number[0] == '0':
        phone_number = '256' + number[1:]
    else:
        phone_number = number

    sms = gateway.sendMessage(phone_number, message, from_="GETIN")


    # if sms is not None and sms.status == "Success":
    #     return True
    # else:
    #     return False