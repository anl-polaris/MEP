import boto3
import base64
from pprint import pprint

def mep_test():
    # start a session connecting to AWS Lambda
    session = boto3.Session()
    client = session.client('lambda')

    # load the test file
    pos_test = "test_mep_scenario_ace.json"
    with open(pos_test, 'r') as f:
        data: str = f.read()

    # send the request to invoke the lambda
    response = client.invoke(
        FunctionName='mep-dev-mep-validation',
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=data
    )

    # read the response
    response['Payload'].read()
    pprint(response)


if __name__ == '__main__':
    mep_test()
