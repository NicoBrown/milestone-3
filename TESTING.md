## Manual testing.

During the development of the application variables were written to the console as the project was built, this enabled confirmation of the required values in a step-by-step process. A local development environment was set up to enable testing of the database functionality as features were added. Flasks built in error handlers were very useful for determining what caused any issues during development. 

Testing the database functionality locally before deployment revealed a number of issues:

- When developing my database models I had mixed the use of class names and database names when referring to foreign keys, leading to the tables not being found
  when queries by SQLalchemy.
- I created tables with capital names and also lower case, this was fixed by dropping the enitre database schema and provisioning a new one to start from scratch.
- I repeatedly got the Jinja templating brackets confused {{ }}, {% %} and where to use each as a function or reference a variable.
- my original database design I created had a many-to-many relationship between "users" and "children". I had planned to store the keys in an array and access them using the following [guide](https://www.postgresql.org/docs/current/arrays.html#ARRAYS-ACCESSING). I could not get the back references working for this kind of relationnship and had to revert to the simplified database design below:

![image](https://user-images.githubusercontent.com/69271605/194314860-dadc7b33-15ef-4c50-94be-769ea4920ec0.png)

Long term I would like to add this functionality into the application to allow it carers and other app users to be invited to a view and update a childs records.

### Bugs encountered at deployment:
- When the app was delployed it couldnt reference the correct database tables, the fix for this was to create the tables within the app context on the heroku CLI:

```
from main import app,db
with app.app_context():
    db.create_all()
    
```

this was taken from this thread on [Stack overflow](https://stackoverflow.com/questions/68445323/basic-flask-app-not-creating-table-in-heroku-postgres-database)

## Automatic Testing
### HTML
The W3C html checker was used on each of the projeects template pages to determine if there were any errors. All templates produced errors related to missing elements such as `head` and `title` because they were used to extend the base.html file which contained those elements, They also had errors related to using Jinja temaplting for the url routes which contained sets of curly braces. The errors specifically relating to templates are below:

- add_child.html 
  - Duplicate attribute type
  - Unclosed element div
  - End tag form seen, but there were open elements
  - Bad value button for attribute type on element a: Subtype missing.
- add_record.html
  - Attribute maxlength is only allowed when the input type is email, password, search, tel, text, or url.
  - Attribute type not allowed on element textarea at this point.
  - Bad value button for attribute type on element a: Subtype missing.
  - The value of the for attribute of the label element must be the ID of a non-hidden form control.

CSS
The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors in the project.

Javascript


Accessibility testing


Further Testing
Known Bugs
