## 1 .Email-Confirmation, i18n, l10n
### Email-Confirmation
The user will get a confirmation email after registering. Then, the user has to click the link inside the email in order to activate the account. It also provides a way to re-send email if the confirmation expires.<br>
### Internationalization (i18n)
The process of changing your contents, so that contents are not only one language, locale, culture, and so on.<br>
### Localization (l10n)
The process of adding the appropriate resources to the API depending on language, locale, culture.  Can be executed many times if necessary.<br>
<br>

## 2 .Upload_image
Allow clients to store images into database via post HTTP requests. Then, it also allows clients to update, delete images. Every client has personal folder to store images. It uses the JWT to retrieve user information(user_id in this case). After that, use that information to create a personal folder for storing images.<br>
<br>


## 3 .Database-Migrations
Migration is very powerful tool, which can manage and alter your database. It tracks the records of a database, so that all you have to do is upgrade or downgrade your database. In short, users can store many versions of records for database.

### Start using migration
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
Modifying code -> flask db migrate -m "comments" -> Checking script -> flask db upgrade

