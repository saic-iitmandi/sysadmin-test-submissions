## Approach
1. I first of all used exiftool to know about the image, but got a very large terminal flooding stream of words!!

2. I then used exiv2 to get details about the chunks present. Suspiciously i found the zTXt chunk to be of seemingly large size.

3. Then i Extracted the text kept in another text file, and as suspected it was 47.0mb in size!!!!

4. I then analyzed the contents of the extracted texts and found that it contained:
    - Total : 9000000 words 
    - Unique : 66 words

5. Then I thought of it like base64 with {,} (curly braces) as the 2 extra chars and tried to decode, if I could find the flag
    - Firstly I created a mapping accoding to the unique word's occurence order. E.g first unique word coin = 'A', etc... to map them to base64 chars + { + } = 66 chars. Then I decoded the extracted text using this decoding, but no flag of `SAIC{.....}` format found.
    - Then I took all unique chars and sorted them then created the map. i.e. First word after sort, 'api' = 'A' and so on. Still didn't got any flag.

6. Then I created a frequency map to get frequencies of each word, and found that 28 words are having the frequency around ~214k and 38 words are having around ~77k.
    - So, I thought that the first 28 chars might be A-Z, {, } and the last 38 might be a-z,0-9,+,/. But this mapping also not yielded anything useful.
    - Then I thought, the last 2 digits of each frequency may tell the equivalent ascii char (dec -> ascii). But then I found that the unit chars are repeating and not including all the chars.
    - Then I thought if some other combination of 2 or 3 digits might reveal something,so I tried checking the [-3:-1] digits, then [-4:-2] digits then [1:4] digits but still did not found anything.

Then I did not understand what to do so I could not proceed from this point.