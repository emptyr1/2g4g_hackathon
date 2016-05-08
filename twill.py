from flask import Flask, request, redirect
import twilio.twiml
import sys
import wolframalpha
import duckduckgo
import pymongo

app = Flask(__name__)

###### wolframalpha
app_id='5LHPH2-T4PVG98PHY'
client = wolframalpha.Client(app_id)

###### DUCK DUCK GO


###### IBM watson 'DIALOG' api

##### mongoDB



@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming text with a simple text message."""
    account_sid = request.values['AccountSid']
    input_text = request.values['Body']

    #print input_text
    twil_resp = twilio.twiml.Response()
    input_text = input_text.encode('ascii','ignore')

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
            twil_resp.message(duck_query.related[2].text)
            print len(duck_query.related)
            final_response = str(twil_resp) + '..press for more...'
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
