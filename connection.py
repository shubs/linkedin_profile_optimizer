from linkedin import linkedin

from linkedin.models import LinkedInRecipient, LinkedInInvitation
import json
import time
import webbrowser
import os
import subprocess
import signal
import psutil

CONSUMER_KEY = '77mdob21napbd1'
CONSUMER_SECRET = '4yPxqdCb3hLodTUV'
USER_TOKEN = "1a817617-f118-4c12-8025-84e0d89132a8"
USER_SECRET = "c331a7f6-7af5-4da5-a886-d182bfbcca75"

RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())
application = linkedin.LinkedInApplication(authentication)


p = application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
# Search URL is https://api.linkedin.com/v1/people-search:(people:(first-name,last-name))?keywords=apple%20microsoft



# application = linkedin.LinkedInApplication(authentication)

# recipient = LinkedInRecipient(None, 'john.doe@python.org', 'John', 'Doe')
# print recipient.json

# invitation = LinkedInInvitation('Hello John', "What's up? Can I add you as a friend?", (recipient,), 'friend')
# print invitation.json

# application.send_invitation(invitation)