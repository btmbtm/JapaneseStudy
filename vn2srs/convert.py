#!/usr/bin/env python
#-*- coding: utf-8 -*-

import glob, os, subprocess, time, sys

def mkPath( path, ext ):
    fdir, fname = os.path.split( path )
    fname_ = fname[:-3] + ext
    path_ = os.path.join( fdir, fname_ )
    return path_

def bmp2png( path ):
    print 'Converting bmp2png for %s' % path
    path_ = mkPath( path, 'png' )
    ret = subprocess.call( [ 'convert', path, path_ ], shell=True )
    if not ret:
        os.remove( path )

def wav2mp3( path ):
    print 'Converting wav2mp3 for %s' % path
    path_ = mkPath( path, 'mp3' )
    ret = subprocess.call( [ 'lame', '--preset', 'standard', path, path_ ] )
    if not ret:
        os.remove( path )

def loop():
    baseMediaDir = sys.argv[1] if len( sys.argv ) > 1 else 'media'

    paths = glob.glob( baseMediaDir+'/audio/*.wav' )
    if len( sys.argv ) > 2 and sys.argv[2]:
        paths += glob.glob( baseMediaDir+'/misc/*.wav' )

    [ wav2mp3( p ) for p in paths ]
    [ bmp2png( p ) for p in glob.glob( baseMediaDir+'/img/*.bmp' ) ]

def main():
    print 'Usage: ./convert.py [baseMediaDir] [alsoProcessMisc]'
    print 'Starting daemon'
    try:
        while True:
            loop()
            time.sleep( 60 )
    except KeyboardInterrupt:
        print 'Shutting down'

main()
