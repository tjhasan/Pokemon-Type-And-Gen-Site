# 4300Final

The code in this project wont run unless you have the following things setup first:

- Be sure that the following location is setup in the /etc/nginx/nginx.conf file
```
        location ^~ /types/ {
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:4301;
         }

        location ^~ /gens/ {
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:1234;
         }

        location ^~ /final/ {
            index index.html;
            alias /home/student/projects/final/;
        }

```

- Be sure that the project directory is located in the following structure:
```
/home/student/projects/final
```

- In order to get the APIs running for the html file to pull from, you need to run the following commands:
```

Command to run gens:

screen uwsgi --socket 127.0.0.1:1234 --wsgi-file /home/student/projects/final/gens.py --master


Command to run types:

screen uwsgi --socket 127.0.0.1:4301 --wsgi-file /home/student/projects/final/types.py --master

```
- Be sure to do "Ctrl-a Ctrl-d" to run the screens in the background. 
## Left To Do:

- Query String
  - As the site is right now, the APIs return the entire database and NOT based on a Query String.
  - We need to change the logic of the API pages and the html pages to accommodate Query Strings.

- Styling
  - The website is made with vanilla HTML. No CSS is currently added to the sites. 
  - The	main site is very simple with just 2 links to both sites. We need to make it more interesting.
  - The	images on the generations page are all different sizes. We need to standardize all the sizes.

- Documentation
  - According to the final project document, we need to have the following documentation:
    - The URI and purpose of each HTML page
    - The URI and purpose of each API, including the query string parameters expected and how they are used.


