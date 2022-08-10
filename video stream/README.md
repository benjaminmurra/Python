# CSCI 3171 (Summer 2021) Assignment 2
Name: Benjamin Murray   
Date: July 22nd 2021
B00: B00636179
Dal E-mail: benjamin.murray@dal.ca


## How to Run

To run my program, navigate to the folder "Code" and run the command:
py Server.py 1050

Then, in a second terminal, run the command 

py ClientLauncher.py 127.0.0.1 1050 5008 movie.Mjpeg

## Program Description

Programming language: python

Client.py

programmed sendRtspRequest() method, inlcluding Setup, Play, Pause and Teardown requests.
Completed openRtpPort().

Rtp.Packet.py
Completed encode() by added header fields


## Program Design

Client.py
Sends RTSP commands to the server by pressing SETUP, PLAY, PAUSE and TEARDOWN buttons.

RtpPacket
Encodes the video data into RTP packets by encoding each frame of the video into a single packet and then sends it via UTP to display on the client's video player. 



## Attributions and References

References here, according to the Dalhousie Academic Integrity Standards.
https://www.dal.ca/dept/university_secretariat/academic-integrity/plagiarism-cheating.html
https://www.dal.ca/faculty/computerscience/graduate-programs/grad-handbook/academic-integrity.html
