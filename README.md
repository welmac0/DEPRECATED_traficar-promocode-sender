
# Traficar Automated Promocode Sender

Automated check of @traficar_pl account on the instagram and sending me an sms with the promo code. I wan't to minimise time spent on the Social Media and pay less for carsharing.

In this project I used TWILIO api in order to send SMS, so please configure your twilio account (It's free) up to yourself. 

## Deployment

To deploy this project all you have to do is just go on Heroku.com and deploy there this app. All files in this repo are already prepared to run there. 

Command to deploy after pushing:
```heroku ps:scale worker=1```
