from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_resources,
)


class AwsCdk2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create queue
        queue = sqs.Queue(
            self, "AwsCdk2Queue",
            visibility_timeout=Duration.seconds(300),
        )
        # create topic
        topic = sns.Topic(
            self, "AwsCdk2Topic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        # create lambda
        sqs_lambda = lambda_.Function(self, "SQSLambda", 
                                      handler='lambda_handler.handler',
                                      runtime=lambda_.Runtime.PYTHON_3_10,
                                      code=lambda_.Code.from_asset('lambda')
                                      )
        
        # create Event Source
        sqs_event_source = lambda_event_resources.SqsEventSource(queue)

        # Add SQS event source to lambda
        sqs_lambda.add_event_source(sqs_event_source)
