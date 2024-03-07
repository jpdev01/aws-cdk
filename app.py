#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_2.aws_cdk_2_stack import AwsCdk2Stack


app = cdk.App()
AwsCdk2Stack(app, "AwsCdk2Stack")

app.synth()
