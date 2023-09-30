# whatsappDictionary
# prerequisities
- create .env file in app/ directory and populate the following variables
```
MONGO_SECRET=
MONGO_USER=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_NUMBER=
TO_NUMBER=
DICTIONARY_KEY=
```

- Enable access from anywhere in the MongoDB Atlas database:

  - Go to your project -> Network Access -> ADD IP ADDRESS -> Access List Entry: 0.0.0.0/0

- configure autktoken for ngrok

# usage
```
docker compose build
docker compose up
ngrok http 8000
```
Set Twilio access point url:

- Go to Twilio console -> Messaging -> Send WhatsApp message -> Sandbox settings -> When a message comes in: `<ngrok_url>/message` Method: POST