Live Chart Demo
===============

Introduction
------------

a live chart demo by flask and canvas.

How to run it
-------------

Run the simulator to generate random data:

    python simulator.py

Open another terminal window to read the data into the database:

    python height_factory.py

Open the third terminal window to run the server:

    python heightApp.py

Finally, rush to the localhost to have a look at the chart:

    127.0.0.1:5000

Note that to run for the first time, users might have to run `python db_init_py_win.py` to initialize the database.
(however, since this version still includes the data files, this step is not necessary.)

How it works
-------------

`db_init_py_win.py` initialize the database.

`simulator.py` simulates some instruments to write data into the egg.csv in a fixed frequency.

`height_factory.py` reads the csv and writes the latest group of data into the database `poolheight.db`.

`heightApp.py` runs as a server which works as follows:

- the user opens the mainpage.
- the page makes some ajax pollings for the data.
- the server looks up the latest data in the database and returns it to the web page.
- the web page draws the live chart by `canvas.js`.

Dependencies
------------

- Python33
- Flask
- Canvas.js(already included)

Note that this runs on windows+python33 in my production envrionment.

What is this anyway
-------------------

This website is one part of the waterpool control system established in SPIA.

Some instrunments detect the height of the water in the waterpool and sends the data to the server.

We want to build a website dealing with the data and displaying them to the users in realtime.

This demo is the prototype of the above part of the system.

Todo
----

This demo will not be maintained for a long time.

Instead, I will implement a more fully-established stuff in another repo lately.

What follows are the features to implement:

- update the data from 6 different places synchronously
- allow the user to look up the history data
- some simple data analysis
- auto-detect the data change in the folder
- some alarm features



