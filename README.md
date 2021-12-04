# Votify

Votify is the backend for a Real-time Voting Application. I made this project as a way to learn the concepts of WebSocket and Asynhronous Gateway Interface.


What it does?


It allows user to log in and gives them a unique ID using UUID.
It allows Candidates (People Contesting the Election) to register themselves and get a unique ID using UUID.


How It Works ?

It works on the principle of WebSocket 2.0., as soon as someone casts a vote, Every one listening to the voting channel would be informed about the current status of Election, i.e. which candidate got how many votes.
