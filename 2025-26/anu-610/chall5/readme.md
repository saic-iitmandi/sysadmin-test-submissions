1. I opened image and just check its property and file type (file image.png) and also zoomed each portion didnt get anything. 

2. then did google to know method to find ctf from image file

3. result also showed first to check file type.

4. then i did strings image.png to check whether any text encoding is inside the image
    it gave too long random string. Then i check the same command with other image to verify this is normal for 
    all image or not. i got the same result for other image also, so i think this will not.
    
5. then i use exiftool to get metadata, there intrestingly i saw some words in discription, and it is too long, so i'm assuming the large file is due to this.

6. then just grep for saic, in this discription ( i know it will be not that much simple, 
    but just for a confirmation :) )

7. then as per search result, i went for binwalk tool. and extracted the embedded files.

8. then went to that extracted folder and cat the first file ( "36" ) it just gave the same thing in description of metadata

9. next file was just empty (95768D)

10. so i decide to move towards steganography

11. for that i use gemini to give methods to find flags hidden in image

12. first thing it said is use zsteg, i installed ruby and then using gem installed zsteg.

13. then as per gemini did zsteg -a final.png to go through all detection methods


14. here is first shows the same big meta description, after that i got something like P0xCB3Ee24c30718F2De29fccfB012f778363e1a06A96, and gemini said it look
    like Ethereum Address if we remove the P. 

    i went to sepolia.etherscan.io and put the address  but didnt matched
