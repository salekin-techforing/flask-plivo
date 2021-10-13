from flask import Flask, request, make_response, Response
from plivo import plivoxml
app = Flask(__name__)

@app.route('/receive_sms/', methods=['GET', 'POST'])
def inbound_sms():

    from_number = request.values.get('From')
    to_number = request.values.get('To')
    text = request.values.get('Text')
    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    return 'Message Received'


@app.route('/reply_sms/', methods=['GET', 'POST'])
def reply_sms():

    from_number = request.values.get('From')
    to_number = request.values.get('To')
    text = request.values.get('Text')
    print('Message received - From: %s, To: %s, Text: %s' %(from_number, to_number, text))

    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.MessageElement(
            "Thank you, we have received your request.",
            src=to_number,  
            dst=from_number))
    print(response.to_string())  # Prints the XML
    # Returns the XML
    return Response(response.to_string(), mimetype='application/xml')


if __name__ == '__main__':
    app.run(debug=True)
