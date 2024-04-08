[https://github.com/celiao/django-rest-authemail](https://github.com/celiao/django-rest-authemail)
says 
Call this endpoint to sign up a new user and send a verification email. Sample email templates are found in authemail/templates/authemail. To override the email templates, copy and modify the sample templates, or create your own, in your_app/templates/authemail.

Your front end should handle password confirmation, and if desired, require the visitor to input their first and last names.

I did this but it did not work so I searched online and found that I need to add the folder to templates path that django recognizes by:
```
'DIRS': [os.path.join(BASE_DIR, 'ats/templates')],
```