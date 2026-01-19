Q5

SAIC{PROOF_OF_PARITY}


the name was proof of parity so i thot it wud have even/odd typeshii

so i checked the file type

> file final.png

it was just a normal png :(
but i had done a similar ctf in the past and flag was in the metadata so tried that

> exiftool final.png

but prob saic peeps were not keeping this easy so ntg was there

then i did Visual Steganography

> strings final.png
 but ntg here
 
 so i thot maybe returning to parity thing and maybe flag is encoded w parity pixels
 
 then made a script (included)
 after running it 
 
 > python3 extract_parity.py
FINALLY got the flag

SAIC{PROOF_OF_PARITY}

