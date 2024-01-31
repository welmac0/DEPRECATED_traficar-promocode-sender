# traficar-promocode-sender
Automated check of @traficar_pl account on the instagram and sending me an sms with the promo code. I want to minimise time spent on the Social Media and pay less for carsharing.

EDIT: 1.12.23 - Doesn't work anymore because Instagram doesn't show description of the posts if you open a profile. You have to <b><i>log in </i></b>, select a photo and then download a description.
    That disables me from this, because I log in via FB, and have 2FA at FB. :(

## Config
Just upload this bunch of files to repo on Heroku, then create a script which initiates the script, add it to scheduler via this add-on:
https://devcenter.heroku.com/articles/scheduler
and that's it.
