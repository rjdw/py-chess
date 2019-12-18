{\rtf1\ansi\ansicpg1252\cocoartf1348\cocoasubrtf170
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural

\f0\fs24 \cf0 READ ME:\
This is a chess AI and a chess game.\
To run, just run the file with python 3\
The 
\i play against friend
\i0 , allows the player to play against another player. This game will not allow illegal moves, and enforces the game until the game is over, which means checkmate.\
After each game, the program stops, and to play another game, you must rerun the file.\
When playing against the AI, the computer uses a Negamax algorithm to calculate the moves 2 - 3 moves deep. \
These moves are evaluated with an evaluation function that considers material weight, and some positionality, mostly in the checks and checkmates of moves.\
Other than that, there are no outside libraries.}