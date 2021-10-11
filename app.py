from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_sms/', methods=['GET', 'POST'])
def inbound_sms():

    from_number = request.values.get('From')
    to_number = request.values.get('To')
    text = request.values.get('Text')
    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    return 'Message Received'

if __name__ == '__main__':
    app.run(debug=True)