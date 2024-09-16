import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_beginner.cdk_beginner_stack import CdkBeginnerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_beginner/cdk_beginner_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkBeginnerStack(app, "cdk-beginner")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
