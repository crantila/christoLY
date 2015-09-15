#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from subprocess import Popen, PIPE

PDF_READER = 'okular'
LILYPOND = 'lilypond'
MUSICXML2LY = 'musicxml2ly'


def christoly():
    if len(argv) < 2:
        print('Usage: python christoLY.py <musicxml_filename>')
        return None
    else:
        print('christoLY.py in Action!')
        filename = argv[1]

    cmd = Popen((MUSICXML2LY, '--lxml', '-o', '{}.ly'.format(filename), filename), stdout=PIPE, stderr=PIPE)
    cmd.communicate(input=None)

    cmd = Popen((LILYPOND, '--pdf', '-o', filename, '{}.ly'.format(filename)), stdout=PIPE, stderr=PIPE)
    cmd.communicate(input=None)

    Popen((PDF_READER, '{}.pdf'.format(filename)), stdout=PIPE, stderr=PIPE)
    # don't wait for the PDF reader to close


if '__main__' == __name__:
    christoly()
