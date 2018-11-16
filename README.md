Python Selenium example, including mobile, headless and proxy configuration.

### Install

Clone this repo, then

> cd selenium-minimal
> virtualenv venv -p python3
> source venv/bin/activate
> pip install selenium

### Run

Make sure to activate the virtual environment:
> source venv/bin/activate

With no arguments:

> python selenium_minimal.py

With all bells and whistles:

> python selenium_minimal.py --mobile --headless --proxy <host>:<port> --user <proxy-user> --password <proxy-pass>
