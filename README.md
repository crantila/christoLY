christoLY
=========

Use LilyPond to Convert a MusicXML File into a PDF

Use
---

Here's how to use "christoLY" to convert a MusicXML file into a PDF.

Open "christoLY.py" in a text editor. Change the PDF_READER variable to the
command of your preferred PDF reader. If you're using Mac OS X or Windows,
you may also need to change the LILYPOND and MUSICXML2LY variables to the
paths of those applications.

Optionally, copy the file to an "installed" location. I do this:

    $ sudo cp christoLY.py /usr/local/bin/christoLY

If you're using Mac OS X or Linux (or a BSD? gasp) make sure your script is
executable. It should be already, but make sure. I do this:

    $ sudo chmod +x /usr/local/bin/christoLY

Now you should be able to run "christLY" as a command from anywhere. If you
want to set christoLY as your MusicXML output program for music21:

    >>> from music21 import *
    >>> settings = environment.UserSettings()
    >>> settings['musicxmlPath'] = 'christoLY'

And that should be it!

Copyright
---------

To the extent possible under law, I have waived all copyright and
related or neighboring rights to christoLY.
