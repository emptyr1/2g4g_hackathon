from flask import Flask, request, redirect
import twilio.twiml
import sys
import wolframalpha
import duckduckgo
import pymongo
from bson.objectId import objectId

app = Flask(__name__)

###### wolframalpha
app_id='5LHPH2-T4PVG98PHY'
client = wolframalpha.Client(app_id)

###### DUCK DUCK GO


###### IBM watson 'DIALOG' api

##### mongoDB

connection = pymongo.Connection()

db = connection["textdb"]
Users = db["textUser"]


cursor = db.Users.find()
for user in db.Users.find():
    print user



@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming text with a simple text message."""
    account_sid = request.values['AccountSid']
    input_text = request.values['Body']

    from_user = request.values['From']
    FromCity = request.values['FromCity']
    FromState = request.values['FromState']
    FromCountry = request.values['FromCountry']

    to_user = request.values['To']
    ToCity = request.values['ToCity']
    ToState = request.values['ToState']
    ToZip = request.values['ToZip']
    ToCountry = request.values['ToCountry']



    result = db.Users.insert_one(
        {
        "Body":input_text
        },
        {
        "account_sid":account_sid,
        },
        {
        "user_all" = [
                {
                    'from':from_user,
                    'FromCity' : FromCity,
                    'FromState':FromState,
                    'FromCity':FromCity,
                    'FromState':FromState


                },
                {
                    'to':to_user,
                    'ToCity':ToCity,
                    'ToState':ToState,
                    'ToZip':ToZip,
                    'ToCountry':ToCountry
                },
            ]
        }

    )

    #print input_text
    twil_resp = twilio.twiml.Response()
    input_text = input_text.encode('ascii','ignore')

    employees.insert({"name": "Lucas Hightower", 'gender':'m', 'phone':'520-555-1212', 'age':8})


    wolf_response = client.query(input_text)
    try:
        wolf_text = (next(wolf_response.results).text).encode('ascii','ignore')
        print wolf_text
        twil_resp.message(wolf_text)
        return str(twil_resp)
    except StopIteration:
        duck_query = duckduckgo.query(input_text)
        print 'hello'
        print duck_query.type
        if duck_query.type.encode('ascii','ignore') == 'answer' or duck_query.type.encode('ascii','ignore') == 'disambiguation':
            twil_resp.message(duck_query.related[0].text)
            print len(duck_query.related)
            return str(twil_resp)

        elif duck_query.type.encode('ascii','ignore') == 'nothing':
            failed_text = 'Sorry, no output for this results, try entering something else'
            print failed_text
            twil_resp.message(failed_text)
            return str(twil_resp)
        else:
            pass




#def query_wolfram(input_text):


if __name__ == "__main__":
    app.run(debug=True)
