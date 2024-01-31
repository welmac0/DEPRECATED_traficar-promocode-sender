# traficar-promocode-sender
This script's goal was to automates the checking of @traficar_pl account on Instagram and sending me an SMS with the promo code. My goal was to minimize time spent on social media and pay less for carsharing.

Edit: 1.12.23 - The script no longer works because Instagram doesn't display post descriptions when you open a profile. Now, you need to log in, select a photo, and then download the description. Unfortunately, this poses a challenge for me since I log in via Facebook, and Facebook has two-factor authentication (2FA).

## Config
Simply upload these files to a repository on Heroku. Then, create a script that initializes the process and add it to the scheduler using this add-on: 
https://devcenter.heroku.com/articles/scheduler
That's it.
