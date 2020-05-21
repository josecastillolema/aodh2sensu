from flask import Flask, request
import requests
import json
# import logging

app = Flask(__name__)
sensu_url = 'http://localhost:4567/results'
PORT=50000

@app.route("/", methods=['POST'])
def jenkins():
   aodh_alarm = json.loads(request.data)
   print (aodh_alarm)
   if aodh_alarm['current'] == 'alarm':
      status = 1
   elif aodh_alarm['current'] == 'ok':
      status = 0
   else:
      status = -1
   sensu_alarm = {
      "source": "aodh",
      "name": aodh_alarm['alarm_name'],
      "output": aodh_alarm['reason'],
      "status": status
   }
   createSensuAlarm(sensu_alarm)
   return "200 OK"

def createSensuAlarm (sensu_alarm):
   body = sensu_alarm
   headers = {
      "Content-Type": "application/json"
   }
   print (json.dumps(body))
   r = requests.post(sensu_url, data=json.dumps(body), headers=headers)

   if r.status_code == 200 or r.status_code == 202:      
      print("The resopnse code is " + r.status.code + ". Message sent succesfully")
      # logging.info("The response code is 200. Message sent succesfully")
   elif r.status_code == 405:
      print("The response code is 405. There was an error")
      # logging.error("The response code is 405. There was an error")
   else:
      print("The response code is " + str(r.status_code) + ". Unknown result")
      #logging.error("The response code is " + str(r.status_code) + ". Unknown result")

   r.text_parsed = json.loads(r.text)
   print(json.dumps(r.text_parsed, indent=4, sort_keys=True))
   # logging.debug(json.dumps(r.text_parsed, indent=4, sort_keys=True))

@app.route("/health", methods=['GET'])
def health():
   return "200 OK"

if __name__ == "__main__":
    app.run(port=PORT, host='0.0.0.0')
