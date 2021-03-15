#!/usr/bin/env python3
import os
import datetime


expiration_timestamp = datetime.datetime.strptime(
         os.environ['AWSUME_EXPIRATION'] , "%Y-%m-%dT%H:%M:%S")

now = datetime.datetime.now()

# if not os.environ.get("AWSUME_EXPIRED"):
    # os.environ.setdefault("AWSUME_EXPIRED","None")
value = "False"
if expiration_timestamp < now:
    # if awsume timestamp is in the past set environment variable
    # os.environ["AWSUME_EXPIRED"] = "True"
    value = "True"
else:
    value = "False"
    # os.environ["AWSUME_EXPIRED"] = "False"

print(f"export AWSUME_EXPIRED={value} ")
