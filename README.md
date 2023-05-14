# Django + ML Job Search API

A Complete Job Search API created using Python / Django as the Backend Language / Framework and Sqlite3 as the Database. It also uses Machine Learning for Recommending Specific Jobs based on the Users Profile

## Endpoints 

- ``` / ``` - Gets a Glimpse of all the Endpoints.
- ``` /getAllJobs ``` - Returns all the Jobs currently available in the Database.
- ``` /get/<id> ``` - Returns Specific Job with an id provided in the id parameter.
- ``` /search?<query> ``` - Returns the Job having a Specific Query.
- ``` /getRelevantJobs ``` - Returns Relevant Jobs based on the users Job Profile.

## Setting Up

Clone or Download the this repository and store it on your machine. 
```bash
git clone https://github.com/arkalsekar/Django-Job-Recommendation-API.git
```

## Usage
Once Downloaded or Cloned the Repository, Run the following Commands

```bash
pip install -r requirements.txt
```
Once Installed all the requirements. Run the Following Commands.
```bash
python manage.py makemigrations
```
```bash
python manage.py sqlmigrate home 0001
```
```bash
python manage.py migrate
```

This is isin't necessary but with this you would be able to login to the website.

```bash
python manage.py createsuperuser
```

This command will finally run the server on localhost://8000
```bash
python manage.py runserver
```
Now head on to [localhost:8000](http://127.0.0.1:8000/) and access the site.


## License
[MIT](https://choosealicense.com/licenses/mit/)
