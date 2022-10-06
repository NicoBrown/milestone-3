<h1 align="center">Baby Journal</h1>
<br> 
<div align="center">
[View the live project here.](#)
</div>
<br> 

### Table of Contents
**[Introduction](#introduction)**<br>
**[Technologies used](#technologies-used)**<br>
**[Design](#design)**<br>
**[User Experience (UX)](#user-experience-ux)**<br>
**[Testing](#testing)**<br>
**[Deployment](#deployment)**<br>
**[Credits](#credits)**<br>

## Introduction

This project is for the milestone project 3 of the Code Institutes Full Stack Developer Course, this Application will allow a user to log baby's daily events. The user can create, read, update and delete baby records for feeding, sleep, nappies and more. 

## Technologies used
  #### Front End
    - materialize UI
    - HTML
    - Custom CSS
  #### Back End  
    - MongoDb
    - Python
    - Flask
    - PostgreSQL
    - Heroku

## Design

### navigation

The home page is designed with a side menu on mobile:

![image](https://user-images.githubusercontent.com/69271605/194311558-5cf16191-f517-4271-b2f3-7fdefd549ec3.png)

and a top menu on larger screen sizes:

![image](https://user-images.githubusercontent.com/69271605/194311725-238db4f4-08c5-41d9-95e6-6115e57355c5.png)


### Colours

### Icons

All icons are from font-awesome

## User Experience (UX)

### Wireframes

The site is designed as mobile-first and to be responsive depending on the user media device. I created low fidelity wireframes in balsamiq cloud to plan the key features of the site which were the home, registration pages and the cards for entering and editing cards.

The home page was deisgned with a hero-image and top navigation bar. The user can use the links to login and register from the nav-bar.
![image](https://user-images.githubusercontent.com/69271605/194308033-c3c16c8b-1269-408c-906a-1fb9de1f7732.png)

when the user logs in they are presented with a home page showing their children, I created a low fidelity wireframe and mapped the links to other screens to help with my required app routing:

![image](https://user-images.githubusercontent.com/69271605/194308312-85e2868a-1fe3-4029-8fdd-9e001784cce4.png)


The childs record page was made into stacked rows and columns at medium and above screen sizes:

![image](https://user-images.githubusercontent.com/69271605/194307008-e4f3b6d1-7f6e-43e8-9e73-5ad1df2e7d9c.png)
![image](https://user-images.githubusercontent.com/69271605/194307851-47b5cc05-e1ba-4285-a6a7-314c9317a3f1.png)

### User Goals

The user must be able to:
- login to the site
- add new children to the site
- record information about a child
- delete a child
- delete and edit a record

## Testing
see [TESTING.md](https://github.com/NicoBrown/milestone-project-3/blob/77c29c106ac823389ca0eea1a823f62922b7eaa2/TESTING.md)

## Deployment

### Heroku

This project is deployed using Heroku. To deploy to Heroku, follow these steps:

1. In GitPod CLI in the root directoy of the project, run: `pip3 free --local > requirements.txt` to create a `requirements.txt` file.
2. In the Gitpod project's root directory, create a new file called Procfile. Open the Procfile, and inside this, check that `web: python3 run.py` has been added or whatever the name of your application happens to be. Remove the blank line at the bottom of the file if that has been created.
3. Login to Heroku, select 'Create new app', add the desired name for your app and choose your closest region, note all names must be unique.
4. Navigate to the Deploy tab on Heroku dashboard and select Github. Search for your repository and when found, click 'connect'.
5. Navigate to the settings tab, click 'reveal config vars' and input the the following:

Key | Value
----|------
DATABASE_URL | ** see below
IP | 0.0.0.0
PORT | 5000
SECTRET_KEY | a_secret_key

** either use your pre configured database url, or provision a postgreSQL database in heroku from the project menu this value will then be pre-populated

6. Return to the Deploy tab and select 'enable automatic deploys'
7. Click 'deploy branch'
8. Click 'Open app' after the build is completed


### github

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/NicoBrown/milestone-3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/NicoBrown/milestone-3)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

The github deployment text was taken from the code institutes template


### Code

the authorisation and login code was taken in part from a previous task project which was created as part of the code institutes coursework.

### Media
 media and images provided by unspalsh

