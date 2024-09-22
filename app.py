#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_lambda_api.cdk_lambda_api_stack import CdkLambdaApiStack


app = cdk.App()
CdkLambdaApiStack(app, "CdkLambdaApiStack")

app.synth()
