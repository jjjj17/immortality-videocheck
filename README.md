# Immortality-Videocheck

## What is it and how to use it

Counting the remaining videos for [**Immortality** by Sam Barlow](https://store.steampowered.com/app/1350200/IMMORTALITY/).

![](https://cdn.cloudflare.steamstatic.com/steam/apps/1350200/header.jpg?t=1705688457)

The following is a script designed to count and identify how many videos you have seen and how many you have remaining, using the log files from the game. I created this because towards the end of the game, finding the remaining videos can be very frustrating. This tool can make that much easier by giving you a file with the remaining videos you have to search for. 

The easiest way to run this script is to use the *rvcounter()* function with your local logs, that can be found most of the time at this location: 

`C:\Users<username>\AppData\LocalLow\Half Mermaid Productions\Immortality\Player.log.`

Running rvcounter with that file will give you a message in this format: 


```
Immortality video count: 
 50 videos have been seen.
 239 remain to be seen. The list of videos to be seen is the following:
 [1, 2, 3, 4, 5, 8, 9, 10, 12, 13, 14, 15, 16, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 133, 136, 137, 138, 139, 141, 143, 144, 145, 146, 147, 148, 149, 150, 153, 154, 155, 158, 159, 160, 161, 162, 163, 164, 165, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 193, 194, 195, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 211, 212, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 227, 230, 234, 235, 238, 239, 240, 241, 242, 244, 245, 246, 250, 251, 252, 253, 254, 255, 257, 258, 259, 261, 262, 263, 266, 268, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289]
``` 


You can also export the remaining list of videos using the *validate()* function, you can see a working example in the [test.py](test.py) script. The test script uses a real (but edited) log and exports an Excel file with the information of the missing videos. The video count and its accuracy were checked by hand.

## Credits

Big thanks to u/Casinocaster and the other contributors to the Reddit list of all the videos and their descriptions. A slightly-edited Excel version of that list was used for the validate method. The original list can be found [here](https://www.reddit.com/r/ImmortalityGame/comments/x43wky/complete_list_of_clips_heavy_spoilers/).

Also, thanks to Sam Barlow and the Immortality team for this great game.

## Contributing

Please, feel free to contribute to the repository. For any further discussion, message me.

### Ideas for contributions:

- [ ] Refactoring code and cleaning up some variable names.
- [ ] Validating that the numbers on the list are the same numbers from the log. This hasn't been checked so far, unless it was done for the original reddit list.
- [ ] Creating a tag system to recommend remaining items/characters to click on.
- [ ] Creating a class for the video list?

## Disclaimers

This script was meant to help players, it is available for free and in no way aims to profit from the original game.

The results of the script depend on the quality and consistency of the logs. In my case, the logs weren't too reliable, but the tool was still useful. The file can still be used with Excel to mark seen videos if you need it.

The content from the list will include **spoilers** from the game. I recommend using this only when you have understood most of the story and going for completionist achievements, like "Cinephile".
