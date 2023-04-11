from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# configure Twilio client
account_sid = "AC04f1fb89a49f05cff7699e7bc70a0826"
# client secret = tZzt1IpBTMJYaUxBy1y0UpIKpcT24Qt9
auth_token = "e611a98423a077094e6fe0d6de858ec5"
client = Client(account_sid, auth_token)

# define route to handle incoming requests
@app.route('/send_message', methods=['POST'])
def create_script_request():
    # retrieve data from request body
    data = request.get_json()
    to = data['to']
    body = data['body']

    # create a new script request
    # your code to create the request goes here

    # send an email notification using Twilio SendGrid API
    message = client.messages.create(
        to=to,
        from_='+15075954898',
        body=body
    )
    print(message.sid)

    # return response
    return {'message': 'Script request created successfully'}

if __name__ == '__main__':
    app.run(port=5005, debug=True, host='0.0.0.0')