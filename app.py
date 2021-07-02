from dotenv import load_dotenv
load_dotenv()

import os
import random
import time

from helpers.claim import Claim

import ldclient
from ldclient.config import Config

# Setup client
ld_sdk_key = os.environ.get('LD_SDK_KEY')
ldclient.set_config(Config(ld_sdk_key))
ld_client = ldclient.get()

# Send an event for a new random context
def send_event_data():
    ## ==================================== ##
    ## Replace this function with your code ##
    ## ------------------------------------ ##
    
    claim = Claim()
    direct_deposit_enabled = ld_client.variation("payment-direct-deposit-option", claim.context, False)
    claim.debug()
    
    if direct_deposit_enabled:
        ld_client.track('Adjusted cost to process claim', claim.context, {}, claim.operational_cost)
        ld_client.track('Claim Resolution Time', claim.context, {}, claim.resolution_time)
    else:
        # Apply adjustments to the control
        claim.adjust_cost()
        claim.adjust_resolution()
        
        ld_client.track('Adjusted cost to process claim', claim.context, {}, claim.operational_cost)
        ld_client.track('Claim Resolution Time', claim.context, {}, claim.resolution_time)

# Send a lot of events for a bunch of random contexts
def create_fake_data():
    for i in range(random.randint(100, 400)):
        send_event_data()

# Loop over a couple times to send several delayed iterations of fake data
number_of_iterations = 10

for i in range(number_of_iterations):
    time_to_wait = random.randint(10, 30)
    
    create_fake_data()
    time.sleep(time_to_wait)

ld_client.close()
