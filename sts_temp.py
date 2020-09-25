#https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-console.html

# curl -X POST -d '{"gremlin":"g.V().limit(1)"}' https://your-neptune-endpoint:port/gremlin
# curl -G "https://your-neptune-endpoint:port?gremlin=g.V().count()"


import boto3
from boto3.session import Session

# run this in ec2
def assume_role(arn, session_name):
    """aws sts assume-role --role-arn arn:aws:iam::00000000000000:role/neptune-db-role --role-session-name example-role"""

    client = boto3.client('sts')
    account_id = client.get_caller_identity()["Account"]
    print(account_id)

    response = client.assume_role(RoleArn=arn, RoleSessionName=session_name)

    session = Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                      aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                      aws_session_token=response['Credentials']['SessionToken'])

    #export AWS_ACCESS_KEY_ID = access_key_id
    #export AWS_SECRET_ACCESS_KEY = secret_access_key

    client = session.client('neptune')

    # connection logic




