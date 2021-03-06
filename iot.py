#!/usr/bin/env python

import os
import json
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

class Listener:
    """
    Params:
    name: string naming the handler
    iot: IoT object created with `createIoT`
    action: callback taking the name of the thing being controlled and the new state value
    """
    def __init__(self, name, iot, action):
        self.name = name
        self.action = action

        # Shadow Handler Doc: https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/index.html
        self.shadow = iot.createShadowHandlerWithName(name, True)
        self.shadow.shadowRegisterDeltaCallback(self.newShadow)
        self.set(False)

    def set(self, payload):
        state = json.loads(payload)['state']['value']
        print('Turning %s to state %s' % (self.name, state))
        self.action(self.name, state)

    # Takes JSON update, a callback, and a timeout in seconds
        self.shadow.shadowUpdate(json.dumps({
            'state': {
                'reported': {
                    'value': state
                    }
                }
            }
        ), None, 5)

"""
endpoint: string containing the URL to hit at AWS (e.g., "xxxxxxxxxxxxxxx.iot.us-east-1.amazonaws.com")
"""
def createIoT(endpoint):
    if os.path.exists(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'AmazonRootCA1.pem')) == False:
        print("Missing certificate file")
        return None
    iot = AWSIoTMQTTShadowClient('UNLSOCIoTTest', useWebsocket=True)
    iot.configureEndpoint(endpoint, 443)
    iot.configureCredentials(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'root-CA.pem'))
    iot.configureConnectDisconnectTimeout(10)  # seconds
    iot.configureMQTTOperationTimeout(5) # seconds
    iot.connect()
    return iot

def action(name, state):
    print("Acting on %s to change to state %s" % (name, state))

if __name__ == "__main__":
    endpoint = "a1lvfv6g3q24e7-ats.iot.us-east-1.amazonaws.com"
    iot = createIoT(endpoint)
    if iot is None:
        print("Failed to create iot item")
    else:
        Listener('test-item-shadow', iot, action)

        print('Listening...')

        while True:
            time.sleep(1)
