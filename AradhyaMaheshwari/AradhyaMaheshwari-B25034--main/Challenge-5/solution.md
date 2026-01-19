## 🔍 Step 1: Initial File Inspection

The provided file is a PNG image.
At first glance, it appears to be a harmless aerial photograph of a campus located in a hilly, green region.

### Actions performed:

-Opened the image using a standard image viewer

-Checked for any immediately visible text, symbols, or distortions

### Observation:

-No visible text

-No QR codes

-No obvious steganographic artifacts

-Image appears clean and professionally captured

## 🧪 Step 2: Steganography & Forensic Checks (Ruling Out Hidden Data)

Even if the image looks normal, CTF methodology requires verifying whether hidden data exists.

### Techniques Considered

-Metadata inspection (EXIF)

-LSB steganography

-Bit-plane analysis

-Embedded files (ZIP/audio/etc.)

-Alpha channel manipulation

### Result:
- Found this symbol (美) when used https://imagetotext.online . This is an chinese letter which in english translates to beauty .
  
- No hidden payload detected

- No suspicious compression artifacts

- No appended data after PNG IEND chunk


## 🧠 Step 3: Common Sense
Since we have tried most of the techniques used for ananlysis of the image and found nothing it means that the answer is of something of common sense . Since , the given image is of IIT MANDI north campus , the most logical answers could be
# SAIC{美}
# SAIC{BEAUTIFUL_IITMANDI}
# SAIC{IIT_MANDI}
# SAIC{NORTH_CAMPUS}

