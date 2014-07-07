#! /usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from os import system

## This script converts from MusicXML to PDF via LilyPond
print( "christoLY.py in Action!" )
#print( "Convert a MusicXML File to LilyPond and Display It" )
#print( "--------------------------------------------------" )

## Make sure we have a file name!
if ( len(argv) < 2 ):
   print( "Usage: python christoLY.py <musicxml_filename>" )
   quit()

#print( "Using MusicXML file: " + argv[1] )

## Options
musicxml2lyProgramOutput = '/home/crantila/musicxml2ly.log'
lyProgramOutput = '/home/crantila/lilypond.log'
pdfReader = 'okular'

## Later, I hope to add in some sort of sanity check here
filename = argv[1]

system( 'musicxml2ly --lxml -o ' + filename + '.ly '+ filename + ' &> ' + musicxml2lyProgramOutput )
system( 'lilypond --pdf -o ' + filename + ' ' + filename + '.ly &> ' + lyProgramOutput )
system( pdfReader + ' ' + filename + '.pdf &' )
