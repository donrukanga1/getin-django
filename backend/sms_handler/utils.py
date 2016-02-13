from backend.sms_handler import AfricasTalkingGateway
from getin.settings import SMS_GATEWAY_USERNAME, SMS_GATEWAY_API_KEY

gateway = AfricasTalkingGateway(SMS_GATEWAY_USERNAME, SMS_GATEWAY_API_KEY)

def send_sms(number, message):
    sms = gateway.sendMessage(number, message, from_="GETIN")

    if sms.status == "Success":
        return True
    else:
        return False