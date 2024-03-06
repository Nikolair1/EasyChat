# Easy Chat

Easy Chat is a simple real-time chat application built using WebSockets and Django Channels. 
It allows users to communicate with each other in real-time, share messages, and view chat history on any device.
The application features a clean and intuitive user interface, making it easy for users to join chat rooms, send messages, and interact with other users. 

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

Key features of Easy Chat include:
- Real-time messaging using WebSocket technology
- User authentication and authorization
- Message persistence for viewing chat history
- Responsive design for seamless user experience across devices

## Requirements

To run this Django project, you'll need the following:

Python Version: Python 3.8 or higher
Django Version: Django 4.2.3
Additional Dependencies:
channels==4.0.0
daphne==4.1.0
You can install all the required dependencies by running:
pip install -r requirements.txt

## Installation

After cloning into the repository, you should get your local machine's hostname.
$ hostname

Then, open two terminal windows.
In the first one run ./runserver.sh which will start the Django server.
And in the second one run ./rundaphne.sh which will start the Daphne server running WebSockets.
Then connect your devices to the local server by going to {hostname}:8000.

## Usage
Once the server is running, users must log in first to start sending and receiving messages.

![image](https://github.com/Nikolair1/EasyChat/assets/93243326/bf62f7ad-c516-493a-afd4-40198e1a2a72)

After hitting the log in button on the ribbon, users can enter any name they would like, as long as it is unique, and will be redirected back to the home page.

![image](https://github.com/Nikolair1/EasyChat/assets/93243326/9e98892f-2694-4b8d-9831-aea65f2be577)

After logging in, users can engage in real-time chat, where their messages are highlighted in blue, alongside other messages. The chat updates dynamically, eliminating the need for manual page refreshes.

![image](https://github.com/Nikolair1/EasyChat/assets/93243326/2aebb2d1-e94f-4ac8-bd4d-bcd321acb728)

Finally, users can see their message history by clicking the history button in the ribbon.

![image](https://github.com/Nikolair1/EasyChat/assets/93243326/13d26508-89e1-4308-be35-c78d443279d8)


Note: To clear all users and messages, one can either access the django admin site or delete the db.sqlite3 database.

## License

MIT License

