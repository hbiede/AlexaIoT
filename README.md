# IoT Setup

## Usage

1. Login to AWS: https://d-90676beed6.awsapps.com/start#/
1. Switch to N. Virginia us-east-1
1. Create an AWS IoT 'thing' via the IoT dashboard
1. Copy endpoint for newly created AWS IoT 'thing' into `iot.py`
1. Create action function in `iot.py` and pass to `Listener` class
1. Activate 'thing' via Alexa

## Utility

This file is useful to allow a server (e.g., [Raspbery Pi](https://www.raspberrypi.org) or Intel NUC) to receive commands from an Amazon Alexa and act on them.
Currently only supports boolean states.

## Roadmap:
Lambda Support
Raspberry Pi usage examples
