# Steps through which I created the program

## Step 1: **Learning Web Scraping through Selenium**

- This was the primary challenge I faced. I tried to "LLM" my way through the problem.
- But since I knew little to nothing about such libraries, I eventually gave up on that approach and started learning web scraping and sending requests.

## Step 2: **Understanding the website and finding the most optimal approach**

### Problem 1 - The Login

- The first task was to log in to the server, which was not a big issue. It was handled by simple `driver.find_element(By.NAME, "field_name")` statements.
- I cleared the fields, entered the credentials, and clicked on the login button.
- This reloads the page. Now that I have access to the booking URL, I can use that from now on.

### Problem 2 - Travel Date Field

- I struggled with this a lot, as my initial approach was to simply click on the field and enter the travel date. This worked fine for a few tries but eventually stopped working.
- Later, I decided to separate the date and the month and filter based on that. This is why my input follows the format `(dd month)`.
- _This approach works amazingly because it automatically filters bookable dates—if a date is unavailable, it won’t be found, saving me the trouble of handling special exceptions._

### Problem 3 - Route and Schedule Field

- After dealing with the Travel Date field, this wasn't as difficult, so I’m grouping these two together. A bit of HTML inspection helped in handling this.
- For the Schedule field, I had to explore further to find a way to filter all available times and select one.
- I discovered that all option titles contained `"AM"` in their string, regardless of whether they were for AM or PM, so I used this to my advantage.

### Problem 4 - Bus No Field

- Filtering this was quite challenging for me at this stage. I initially planned to display a list of available buses, but filtering them out proved tricky.
- Fortunately, the problem statement required me to hardcode the bus name, so it could run periodically at the scheduled time.
- Thus, I filtered the available options and selected only the bus I needed.

### Problem 5 - Selecting the Bus Seat

- I observed that all vehicles had a maximum of 30 seats and found a general pattern for their checkbox ID:  
  `checkbox{i}`  
  where `i` ranges from 1 to 30.
- From there, I checked for disabled seats and filtered them out.
- Finally, I clicked on "Save" to confirm my selection.

## Step 3: **Understanding Email Handling Through Python**

- Will not lie, GPT helped me with this as I had not learned it yet. I just learned enough for it to send me a mail after this task completes.
- It was a pleasure learning this, though.

## Step 4: **Dealing with Automation of the File**

- I had little experience here as well, but due to guilt of using GPT, I preferred to learn this and then complete the task.
- It took me a while to get a hang of it, starting by printing a sentence every minute to eventually including error handling.

# Conclusion

- I did use ChatGPT to learn a lot of things required in this task as well as to debug a few mistakes I made.
- But honestly, I would love to thank the SAIC team for giving me this opportunity to learn something new.
