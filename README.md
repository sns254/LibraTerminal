# LibraTerminal
Very basic command line wallet for Libra, written in Python.

Uses bandprotocol's <a href="https://github.com/bandprotocol/pylibra">pylibra</a> module.

Currently, only whole amounts of Libra can be transacted with. Only five accounts are generated, but the code can easily be tweaked to accommodate more.

<h2>Setup</h2>

Navigate to the desired directory.

`mkdir LibraTerminal && cd LibraTerminal`

Create a virtual environment:

`virtualenv librawallet`

Activate it:

`source librawallet/bin/activate`

Get the necessary Python modules:

`pip3 install pylibra`

`pip3 install termcolor`

`pip3 install pyqrcode`

Now create a new file:

`sudo nano wallet.py`

Copy the contents of this repository's <b>wallet.py</b>, paste them into your text editor and save it (`CTRL-X`, select 'y' when prompted).

Now we can run it:

`python3 wallet.py`

Don't forget to deactivate the virtual environment when you're finished.

`deactivate`
