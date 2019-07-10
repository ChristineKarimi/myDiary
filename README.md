# Mini Diary

#### An application that allows users living their best lives to share their experiences and adventures with their online friends. Keep in touch with their fellow fun loving friends and recommend fun activities or places to other people. 

#### Built by Chris

## Description
View live site: coming soon

This is a web platform for users living their best lives to share their experiences and adventures with their online friends. Users create an account to join a community and can share of any memorable experience they might have been part of. Users can also reccomend certain activities to other people by sharing images and posting reviews. 

## App
![Landing Page]()
![Shared memories page]()
![Profile Page]()

## Setup/Installation Requirements
* Ensure you have python and pip installed beforehand.
* Clone the project using this command <br/>
`https://github.com/ChristineKarimi/miniDiary.git`
*  After cloning,navigate into the folder <br/>
 `cd miniDiary`
 * Install the virtual environment using the following commands<br/>
 `python3 -m venv virtual`
* Activate virtual environment using the command below<br/>
  `source virtual/bin/activate`
*  Install all the required depedencies in the virtual environment<br/>
  `python3 -m pip install -r requirements.txt`
* Run `$ python manage.py runserver` to serve the application.<br/>
* The application should work at this point.

## Behavior Driven Development (BDD)
| Behavior | Input    | Output   |
| :------------- | :------------- | :------------- |
| User authentication | click on the sign up button  | registration form |
| Profile editing | Click on edit profile button  | profile page form|
| User can view details of a single post | Click on a specific post  | Profile page details form |
| User can search for specific stories | Input a keyword on the search bar | Results-page |
| User can view stories related to what their interests| Clicks on shared posts button| Feeds Page |

## Known Bugs
Some of the features are still under development and will be constantly updated. 

## Technologies Used
The application is built on:
* Python3
* Ajax
* Bootstrap 4
* Django 1.11 framework
* Postgresql 

## Support and contact details
For any queries and suggestions, please contact the support team via **Email: karimikim3@gmail.com**

### License
*MIT License*

*Copyright (c) [2019] [CHRIS]*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

*THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*
Copyright (c) 2019 **christine Karimi**
