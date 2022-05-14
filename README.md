# Simple-one-player-Pong
--Use "a" key to start/stop the ball/ai movement
--w and s keys are used to move your character up and down
--You play as the blue character
--speed and hitbox size are measured in screen pixels
--intended for 1920x1080 display, haven't been able to test on others
--difficulty levels go as follows:
1. ~50% chance to move randomly, ~50% chance to move towards y coordinate for playball (green)
2. ~40% chance to move randomly, ~60% chance to move to y coordinate of playball (green)
3. moves to y coordinate of playball, + it's upwards momentum
4. calculates location as to where playball will contact the end of screen, ignores bouncing off the bottom/top of screen
5. originally was going to be one that would calculate the exact location of where the ball and edge of screen would meet, sadly had technical difficulties


--"COMPUTERSCIENCEFINAL" is the final version (as of now, will probably continue for fun)

--2-player-pong is a 2 player version, with signicant ghosting issues, should be an easy fix

--Xbox controller support in the future maybe?
--colour picker maybe?
--speed doesn't update until the playball (green) contacts a x-border or red/blue ball
