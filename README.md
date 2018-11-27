# flask-restful-api-features

# 1 .Email-Confirmation, i18n, l10n
## Email-Confirmation
The user will get a confirmation email after registering. Then, the user has to click the link inside the email in order to activate the account. It also provides a way to re-send email if the confirmation expires.<br>
## Internationalization (i18n)
The process of changing your contents, so that contents are not only one language, locale, culture, and so on.<br>
## Localization (l10n)
The process of adding the appropriate resources to the API depending on language, locale, culture.  Can be executed many times if necessary.<br>
<br>

# 2 .Upload_image
Allow clients to store images into database via post HTTP requests. Then, it also allows clients to update, delete images. Every client has personal folder to store images. It uses the JWT to retrieve user information(user_id in this case). After that, use that information to create a personal folder for storing images.<br>
<br>


# 2 .Database-Migrations
## Start using migration
1. Go to the folder where contain app.py, create migrations folder 
```
flask db init
```
2. Create all tables, it generates versions file inside migrations folder
```
flask db migrate
```
