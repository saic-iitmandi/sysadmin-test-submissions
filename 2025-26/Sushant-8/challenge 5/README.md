# MY ATTEMPT TO FIND THE FLAG

My first clue was the file size of **final.png** being too large for a simple **650x481** image: **10 MB**.  
I knew that the image itself was a container. I also looked in details and activity of the Google Drive folder and the image preview, but no clue was there.

I then used the resource of **ctf101.org – forensics section** extensively.  
I used **Gary Kessler's tool** and found that it was just a PNG image.

Running:

exiftool final.png

flooded my terminal, but I then exported it into **metadata.txt**. Still no clue was there.  
However, I found a pattern that **all words in the description were of 4 letters**.

---

## The Most Exhausting and Tinkering Part

I assumed a lot of things and tried finding patterns. ChatGPT wrote some code for me to test ideas.

Here is the list of methods for which I tried finding the flag:

- vowel parity  
- alphabet position sums  
- scrabble scores  
- keyboard left/right parity  
- run-length parity  
- prime index selection  
- first/last letter streams  also i tried manmade vs natural objects 1/0 encoding

Each attempt produced just random noise and I couldn’t really find the **"SAIC{"** pattern.  
Although the data looked meaningful when converted through ASCII, I couldn’t hit anything.

In one of the patterns I found **"k"** as my first letter which is very close to **S**, but still no success.

---

## Discovery of the Payload

To discover the payload I then used:

pngcheck -7 final.png

It revealed some **compressed zTXt text**.  
So now I thought this was the true data which needed to be analysed.

---

## Extracting the Hidden Core

Then GPT suggested extracting the actual stream using **dd** and **zlib-flate**:

dd if=final.png of=payload.zlib bs=1 skip=9795213  
zlib-flate -uncompress < payload.zlib > payload.bin

The result was structured but not readable.  
Even after some manipulation I couldn’t really get anything from it.

I tried the old trick of reading the **LSB**, but it didn’t work.  
Then I tried reversing them, but still no success.  
I also tried some cipher text ideas, but they also failed.

So I realized the flag is sitting somewhere deep and I am giving this problem a rest as of now.

---

## Other Tools Tried

I also tried some online tools:

- **StegOnline**  
  - In that I found the **blue 0 bit plane**.  
  - It looked random, but at the same time it again looked like a hidden file.

- I extracted the **hex string**, but it was also no good.  
- ASCII text was just not helping.

In StegOnline I somehow created some **.dat file** (sorry, I forgot how I did it) which I converted into **.png**, but it was just not repairing.

---

## Current Status

I could not recover the flag, but I learned:

- Metadata can hide real binary data  
- Not every readable text is actual payload  
- Parity can exist at many layers  

For now I am stopping here.

