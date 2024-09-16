from aws_cdk import (
    # Duration,
    aws_ec2,
    Stack
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkBeginnerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cidr = '10.0.0.0/16'
        vpc = aws_ec2.Vpc(
            self,
            id='test-vpc',
            cidr=cidr,
            nat_gateways=1,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    cidr_mask=18,
                    name='public',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                ),
            ],
        )
