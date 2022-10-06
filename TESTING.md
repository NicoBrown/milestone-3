Manual testing.

A local development environment was set up to enable testing of the database functionality as features were added. This revealed a number of issues:

- When developing my database models I had mixed the use of class names and database names when referring to foreign keys, leading to the tables not being found
  when queries by SQLalchemy.
- I created tables with capital names and also lower case, this was fixed by dropping the enitre database schema and provisioning a new one to start from scratch.
- I repeatedly got the Jinja templating brackets confused {{ }}, {% %} and where to use each as a function or reference a variable.
- my original database design I created had a many-to-many relationship between "users" and "children", I could not get the back references working and had to revert ot the database design below:

![image](https://user-images.githubusercontent.com/69271605/194314860-dadc7b33-15ef-4c50-94be-769ea4920ec0.png)


Bugs encountered at deployment:
- When the app was delployed it couldnt reference the correct database tables, the fix for this was to create the tables within the app context on the heroku CLI:

```
from main import app,db
with app.app_context():
    db.create_all()
    
```

this was taken from this thred on [Stack overflow](https://stackoverflow.com/questions/68445323/basic-flask-app-not-creating-table-in-heroku-postgres-database)
