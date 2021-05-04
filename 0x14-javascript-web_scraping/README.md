## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

## Tasks
### 0. Readme
Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object
	* File [0-readme.js](0-readme.js)
### 1. Write me
Write a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object
	* File: [1-writeme.js](1-writeme.js)
### 2. Status code
Write a script that display the status code of a GET request.
* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request
	* File: [2-statuscode.js](2-statuscode.js)
### 3. Star wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint https://swapi-api.hbtn.io/api/films/:id
* You must use the module request
