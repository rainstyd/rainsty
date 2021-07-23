#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: rainsty
@file:   test_v.py
@time:   2021-05-17 16:35:26
@desc:   
"""

from moviepy.editor import *

video = VideoFileClip('./file/test_v1.mp4')
audio = video.audio
audio.write_audiofile('./file/test_v1.mp3')
