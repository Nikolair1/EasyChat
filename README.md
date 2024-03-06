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
In the first one run ./runserver.sh
And in the second one run ./rundaphne.sh

Then connect your devices to the local server by going to {hostname}:8000

## Usage

Explain how to use your Django project. Provide examples or code snippets to demonstrate usage, and include any additional information users may need to know.

## License

MIT License

