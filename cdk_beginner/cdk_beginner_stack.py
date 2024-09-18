from aws_cdk import (
    # Duration,
    aws_ec2,
    Stack
    # aws_sqs as sqs,
)
import base64
from constructs import Construct

class CdkBeginnerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # vpc
        cidr = '10.0.0.0/16'
        vpc = aws_ec2.Vpc(
            self,
            id='vpc-cdk',
            cidr=cidr,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    cidr_mask=18,
                    name='public',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                ),
            ],
        )

        security_group = aws_ec2.SecurityGroup(
            self,
            id='security-group-cdk',
            vpc=vpc,
            security_group_name='security-group-cdk'
        )

        security_group.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4(cidr),
            connection=aws_ec2.Port.tcp(22),
        )

        # 自分のPCのIPアドレスを取得して、ここに設定します
        my_ip = "0.0.0.0/0"  # 例: "203.0.113.0/32"
        security_group.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4(my_ip),
            connection=aws_ec2.Port.tcp(80),
        )

        # Apacheをインストールするためのユーザーデータ
        user_data_script = """
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        """

        # キーペア作成
        keypair = aws_ec2.CfnKeyPair(
            self, 
            'KeyPairCDK', 
            key_name='key-pari-cdk'
        )

        user_data_base64 = base64.b64encode(user_data_script.encode()).decode()
        image_id = aws_ec2.AmazonLinuxImage(generation=aws_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2).get_image(self).image_id

        aws_ec2.CfnInstance(
            self,
            id='ec2-instance-cdk',
            availability_zone="ap-northeast-1a",
            image_id=image_id,
            instance_type="t2.micro",
            key_name='key-pari-cdk',
            security_group_ids=[security_group.security_group_id], 
            subnet_id=vpc.public_subnets[0].subnet_id,
            user_data=user_data_base64,
        )





