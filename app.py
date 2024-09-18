#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_beginner.cdk_beginner_stack import CdkBeginnerStack


app = cdk.App()
env_JP=cdk.Environment(region='ap-northeast-1')
CdkBeginnerStack(app, "CdkBeginnerStack", env=env_JP)

app.synth()
