from flask import Flask, request
import requests 
import json
import wikipedia
app = Flask(__name__)
ACCESS_TOKEN = "EAAdRvyvoNb8BAEzVXvjaVDgGnWIPRTZCdyp85Hr3cmZBkWgIPUDaZCItVd3McDE4T0fCireOqh95KjL3M9PIZAFftiIgNZCMH9oLl20Mb7nM5fnJX55L94g4xgdi8xsNRC8bndQohZAHPFcVdqBJc6ZBuZASjZBHu6RxrSMfrMNAnMSY0ZC51GMNYW"
@app.route('/',methods=['POST'])
def whoIs():
    # print("hehehehehehe")
    # message = request.json.get("text")
    # print(message)
    # req = ai.text_request()
    # req.session_id = request.json.get('from').get('id')
    # sender = req.session_id
    # req.query = str(message)
    # resp = req.getresponse()
    # msg_df = json.loads(resp.read())
    # print(msg_df)
    if request.method == 'POST':
        msg_df = request.json
        print(msg_df)
        msg_df1 =str(msg_df['result']['parameters']['given-name']) +" "+ str(msg_df['result']['parameters']['any']) + " " +str(msg_df['result']['parameters']['last-name'])

        print(msg_df1)
        # summ = wikipedia.summary(msg_df1, sentences=5)
        id = msg_df['originalRequest']['data']['sender']['id']
        # messenger(summ, id)
        
        # print(wikipedia.summary(msg_df1, sentences=5))
        # return "Kooool"
        try:
            summ = wikipedia.summary(msg_df1, sentences=5)
            return messenger(summ, id)
        except:
            for newquery in wikipedia.search(msg_df1):
                try:
                    summ = wikipedia.summary(newquery, sentences=5)
                    return messenger(summ, id)
                except:
                    pass
        return "I don't know about "+ msg_df1
# firstQuestion="Hi, how are you?"
# Chat("examples/Example.template", reflections,call=call).converse(firstQuestion)
def messenger(message,sender_id):
    data = {
                "recipient": {"id": sender_id},
                "message": {"text": message}
            }
    qs = 'access_token=' + ACCESS_TOKEN
    resp = requests.post('https://graph.facebook.com/v2.6/me/messages?' + qs, json=data)
    print(resp.content)
    return "Hola!"        
if __name__=='__main__':
    app.run(port=50001, debug=True)    