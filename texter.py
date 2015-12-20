from twilio.rest import TwilioRestClient

class Texter:

  SID        = "*****************"
  AUTH_TOKEN = "*****************"
  RECV_NUM   = "************"
  TWILIO_NUM = "************"

  def __init__(self):
    self.client = TwilioRestClient(Texter.SID, Texter.AUTH_TOKEN)

  def text(self, person):
    msg_body = """

    **************
    Who : {0}
    When: {1}
    **************

    """.format(person.name, person.date_str())

    self.client.messages.create(to=Texter.RECV_NUM,
                                from_=Texter.TWILIO_NUM,
                                body=msg_body)
