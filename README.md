## 1 .Email-Confirmation, i18n, l10n
### Email-Confirmation:
The user will get a confirmation email after registering. Then, the user has to click the link inside the email in order to activate the account. It also provides a way to re-send email if the confirmation expires.<br>
### Internationalization (i18n):
The process of changing your contents, so that contents are not only one language, locale, culture, and so on.<br>
### Localization (l10n):
The process of adding the appropriate resources to the API depending on language, locale, culture.  Can be executed many times if necessary.<br>
<br>

## 2 .Upload_image
Allow clients to store images into database via post HTTP requests. Then, it also allows clients to update, delete images. Every client has personal folder to store images. It uses the JWT to retrieve user information(user_id in this case). After that, use that information to create a personal folder for storing images.<br>
<br>


## 3 .Database-Migrations
Migration is very powerful tool, which can manage and alter your database. It tracks the records of a database, so that all you have to do is upgrade or downgrade your database. In short, users can store many versions of records for database.

### Start using migration:
1. Go to the folder where contain app.py, create migrations folder.
```
flask db init
```

2. Create a script inside versions folder, which is inside migrations folder. That script contains code for creating table. In addition, you can add comments for that.
```
flask db migrate -m "comments"
```

3. After checking the script inside the versions folder, you can create the tables, upgrade the database, and so on. remember to modify the python script to specify constraint name.
```
flask db upgrade 
```

4. If you want to check the current version of database, run sql query
```
SELECT * FROM alembic_version;
```

5. Run this command in order to downgrade database, remember to modify the python script to match name constraint.
```
flask db downgrade
```

6. If you want to add a new column in the existing table, modify the code in the models for adding a new column and run this command.
```
flask db migrate -m "add new column in a table"
flask db upgrade
```

### Note:
Modifying code -> flask db migrate -m "comments" -> Checking script -> flask db upgrade<br>


## 3 .OAuth 2.0
 OAuth is a way to log in with a third party. In this case, I use Github API to implement this functionality. First of all, users click the login with Github button in the front end. Then, the client(application) asks API to ask users to authorize the client. The way of asking if users want to authorize the client is sending users to Github page. After authorizing, users would be sent back to the client's redirect URI. The redirect URI contains a code, which is unique to the interaction. After that, the client sends the code and secret information to Github. Therefore, Github knows the client is a real application with those two pieces of information. Then, Github sends access token to the client. Once the client got the token, it can make requests with that token in order to get information of users as long as the client specified that it wants to be able to retrieve this information at first.


### Roles of OAuth 2.0
- User:
Users are whom we want to access data of. They authorize client, which is our application, to access their accounts.

- Authorization/Resource Server(API):
They are companies such as Google, Facebook, Github, and so on. In charge of protecting user accounts. They are able to verify identity of users when they authenticate. After that, API send access tokens to the client. 

- Client:
Client is our application, which wants access to user accounts. However, users have to authorize that access before we access. After that, the API has to validate the authorization. 

### Authorization callback URL:
Where the users will be sent back to after users have authorized our application.

### Client ID:
This is a public identifier that users know about.

### Client Secret:
This would be used for sending post requests to Authorization/Resource Server. It should be kept sercet.
