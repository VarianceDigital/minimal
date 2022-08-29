# Minimal Flask + Boostrap 5 Website Project 

## Overview

In this repo you'll find the source code for a minimal yet complete Flask + Boostrap 5 project, featuring:

- sound structure using Python component and Flask Blueprints, so that the project can scale (to even quite big and complex sites); see section "Project Structure and Settings"
    
- use of modal popus for messages and...
- ... a full fledged cookie banner (with server side management)
- sticky footer (useful when pages are "short" or empty)
- navbar with logo and current section highlighting
- breadcrumb navigation
- in-site SEO friendly features:
    - **100% score on pagespeed insights!**
    - nice urls (slugify)
    - urls following SEO best practice
    - access to sitemap.xml and robots.txt
    - META and CANONICAL tags in `<header>`
    - out of the box http -> https redirect
- custom error pages
- in-page error alert

Bootstrap 5 is used:
- to make the site fully responsive
- for modal popups and the cookie banner
- for the navbar (it's just an easy option)
- for the error alert

Note: Boostrap 5 css and js files are taken from the official Boostrap CDN, but one can go ahead and download (or install) all needed files.

## Requirements and specifications
- The site make use of the Flask session, in a minimalistic way, to manage the cookie settings and policies
- IMPORTANT! secrets are supposed to be retrived from config vars. Running the site locally, these values are taken from main.py. To run the site in production, one MUST setup config vars server side. **Do not** send main.py (with git or similar VCS) to the net.
- The site does NOT use JQuery: Bootstrap 5 now uses vanilla Javascript to show modal popups - and for other interactive behaviours.

### Packages needed, which are present in requirements.txt
All packages needed are listed in the requirements.txt file.
To install, first activate your venv and then:

``pip install -r requirements.txt``

The main packages needed are:
- Flask
- gunicorn
- inflection

### Page structure
Each page has the same main strucutre, having:
- head section (with Boostrap 5 navbar)
- main content section
- footer section (with sticky bottom)

The head and footer sections are implemented with two include files, while the "main content" section is implemented via Flask `block` and `extend` commands.



## Project Structure and Settings

The project runs locally starting from main.py, but is supposed to run in production **bypassing** main.py, by configuring gunicorn as explained below;

### What auth.py blueprint is about


## Running this site on Azure and Heroku
Here we will describe how to deploy this site on Azure and Heroku.