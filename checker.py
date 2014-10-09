import webapp2
from google.appengine.api import mail
import logging
import urllib2
import json


class CheckerHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Checker is being invoked")

        logging.debug("Requesting remote URL")
        response = urllib2.urlopen('http://store.apple.com/sg/buyFlowSelectionSummary/IPHONE6?node=home/'
                                   'shop_iphone/family/iphone6&step=select&option.dimensionScreensize=4_7inch&'
                                   'option.dimensionColor=gold&option.dimensionCapacity=16gb&'
                                   'option.carrierModel=UNLOCKED%2FWW&carrierPolicyType=UNLOCKED')

        logging.debug("Parsing json")
        result = json.load(response)
        option = result['body']['content']['selected']['purchaseOptions']

        if not "Unavailable" in option['shippingLead'] or option['isBuyable']:
            mail.send_mail(sender="<sender>",
                           to="<recipient>",
                           subject="iPhone 6 is now available in Singapore store. Act now!!!",
                           body="Act now.")

        self.response.write('OK')