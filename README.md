# DLSR-WebApp
-----

The hopefully-someday-to-be-more-creatively-named Flask-based application to control a Raspberry Pi connected DSLR.

All this because straight up using the gphoto2 commmand line sounded like a pain. *Sigh*

## Rough Plan

Web application sends REST request to server which is running on a Pi, serving either over WiFi or Bluetooth.
Server is running a Flask application that wraps the gphoto2 library which controls a USB-connected DSLR.
