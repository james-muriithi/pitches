# Pitches
Pitches is where you make your ideas known 
## Description
A flask web application where users can make their pitches, comment and vote for them.

## Setup Requirements
* Git
* Web-browser or your choice
* Flask(1.1.4)
* Pip
* Python 3.8
* postgres

# Setup / Installation
* clone the repo:

```shell
git clone https://github.com/james-muriithi/pitches.git
```

```shell
cd news-hub
```
* create virtual environment 
```shell
python3.8 -m venv --without-pip venv
```

* To activate the virtual environment
```shell
source venv/bin/activate
```

* install the packages from requirements.txt
```shell
pip install -r requirements.txt 
```

* setup environment variables
```shell
cp .env.example .env
```
* Execute the shell script and start the server
```shell
chmod a+x start.sh
./start.sh
```
* open the browser and navigate to http://127.0.0.1:5000/ to see the application in action

## Technologies Used
The following languages have been used on this project:

* HTML
* CSS
* JS
* Bootstrap
* Flask
* Python

## Demo
[Here is a demo of the deployed website](https://pitches-moringa.herokuapp.com/)

## Designs
Here are the Designs
![Design](./screenshots/design.png)
![Design](./screenshots/login.png)
![Design](./screenshots/signup.png)


## Screenshots
![Home Screenshot](./screenshots/screenshot.png)
![Login Screenshot](./screenshots/login-screenshot.png)
![Signup Screenshot](./screenshots/signup-screenshot.png)
![Profile Screenshot](./screenshots/profile-screenshot.png)

## Support and contact details
To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: james.muthike@student.moringaschool.com

## License

Copyright (c) 2021 Moringa school

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files , to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.