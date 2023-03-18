import boto3
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "Spencer Woo <sender@domain.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
RECIPIENT = "recipient@domain.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
# CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-1 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-west-1"

# The subject line for the email.
SUBJECT = "Test Subject"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Hi Spencer,\r\n"
             "Thanks for reaching out!  Yes, I'm interested.  I've completed the article.\n\n"
             "Best, \nSpencer"
            )

REPLY_TO = 'reply@domain.com'
            
# The HTML body of the email.
# BODY_HTML = """<html>
# <head></head>
# <body>
#   <p>Hi Spencer,\r\n
#   Thanks for reaching out.  Yes, I'm interested!\n\n
#   Best,\nSpencer Woo</p>
# </body>
# </html>
#             """            

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                # 'Html': {
                #     'Charset': CHARSET,
                #     'Data': BODY_HTML,
                # },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            # 'Reply-To': {
            #     REPLY_TO
            # },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
        # ConfigurationSetName=CONFIGURATION_SET,
    )
# Display an error if something goes wrong. 
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])


def listEmailAddresses():
    ses = boto3.client('ses')

    response = ses.list_identities(
      IdentityType = 'EmailAddress',
      MaxItems=10
    )

    print(response)

def listEmailDomains():
    ses = boto3.client('ses')

    response = ses.list_identities(
      IdentityType = 'Domain',
      MaxItems=10
    )

    print(response)
