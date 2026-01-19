First I checked the properties of the file to see any unusual thing, like file size and it was written 10 MB. I then ,to check its metadata , installed exiftool and opened a terminal in that folder of exiftool. Then wrote the command .\\exiftool.exe final.png , which showed me a huge paragraph of words. 



The name of the challenge was proof of parity so I tried various patterns in which I can decode the flag. First, I tried assigning the words with odd number of letters as 1 and even as 0. Then I got a long list of sequence of 0’s and 1’s. Then divided then into 8 bit parts and converted to ASCII. I didn’t convert all the words but the starting ones but the letters were not making sense. Then I decided to convert it by seeing the number of vowels in a word and assigning even number of vowels in a word as 0 and odd number of vowels as 1. By doing this I got SAIC{v0w3l\_p4r1ty\_1s\_fun}.  



