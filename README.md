# Basic boilerpate Register, Login and Logout. Python Backend and Vue.js Frontend

A SPA app with frontend made using Vue.js and backend in Python 3.8.
This app has only 3 functions 
* Register - A component to register a new user
* Login - A component to authenticate and generate a JWT for the user session
* Logout - To invalidate the user session.

## Getting Started

Clone the repository 
```
git clone https://github.com/andrebaldo/python-vue-spa-boilerplate.git
```

### Prerequisites

* [Python 3](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/)
* [Vue.js](https://vuejs.org/v2/guide/installation.html)
* [Vue Client](https://cli.vuejs.org/guide/installation.html) 

### Installing

The installation is made in two steps, Backend and Frontend.

#### Database
If you don't have an SQL Server instance in your local machine you can install it downloading the 
"Microsoft SQL Server Express" or change the python file to point to a existing instance.
In your SQL instance create a new database called "project001"

#### Backend
Before you install the python dependencies you need to install the virtualenv and activate it, in order
to do it please execute these commands one by one in a new command prompt window (cmd).
```
cd python-vue-spa-boilerplate\backend
pip install virtualenv
virtualenv venv
cd venv\Scripts\
activate
cd ..
cd ..
```

Using the same command prompt, go to the backend folder (if you are not in there yet) and run the pip install requirements.txt command

```
pip install -r ./requirements.txt
```
Once the pip have installed all the dependencies you need to create the database structure, to do it there is
python script that does it for you, just execute this command:
```
python databaseCreation.py
```
If you didn't get any error, you can run the backend API using this command below:
```
python app.py
```
You can check if the API is running accessign the address http://localhost:5000/home you should receive Unauthorized message, if you got it the API is runing.

Now let us start the Frontend

#### Frontend
Open a new command prompt and go to the frontend folder.
```
cd python-vue-spa-boilerplate\frontend
npm i
yarn serve
```
## Authors

* **Andre Baldo**  [andrelbaldo](https://github.com/andrelbaldo)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

