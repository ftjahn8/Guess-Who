# Guess-Who (written with Python 3.10)

Python-Version of [GuessWho by chadgra](https://github.com/chadgra/GuessWho), which was developed for the Video [BEST Guess Who Stategy- 96% WIN record using Math](https://www.youtube.com/watch?v=FRlbNOno5VA) by Mark Rober.

I rewrote the main script, so it tests all different strategies one after another for 1000 games and calculates the average rounds to win.  
Results of one of my runs:
```
SimplePlayer took on avg: 12.512 rounds to win.
NormalPlayer took on avg: 6.683 rounds to win.
LessThanHalfPlayer took on avg: 5.764 rounds to win.
AlwaysHalfPlayer took on avg: 5.67 rounds to win.
CombinedPlayer took on avg: 5.016 rounds to win.
```

`! These numbers can differ on re-runs in the decimal places. !  `

But you can still see clearly the point of Mark that math helps to win in the game.
We also nearly achieve the average of 5 rounds to win with the CombinedPlayer-Strategy as he stated in the video.

Results of my 2nd runs:
```
SimplePlayer took on avg: 12.454 rounds to win.
NormalPlayer took on avg: 6.799 rounds to win.
LessThanHalfPlayer took on avg: 5.795 rounds to win.
AlwaysHalfPlayer took on avg: 5.698 rounds to win.
CombinedPlayer took on avg: 4.991 rounds to win.
```
