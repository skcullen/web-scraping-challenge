# web-scraping-challenge

Week 12: Web Scraping and MongoDB Homework

Included in this repository is my solution for the Week 12: Web Scraping and MongoDB Homework for the Georgia Tech Analytics Bootcamp.

In this assignment, we were asked to scrape data from several websites, and use that data to populate a page of our own. There were four different websites we were asked to scrape. From the first was an article title and description using BeautifulSoup. The second was a particular high resolution image using splinter. The third was a table of data about mars using pandas. Finally, the last asked to scrape was for photos and their accompanied title.

From there we were asked to use flask in order to set up a page to show the scraped data upon the click of a button.

I ran into several problem in this assignment. When scraping the first website, the prettify() function was giving me some weird redacted version of the cite, so that most of the text and values were missing. I decided to take two paths here. I scraped a value from the shown prettify(), since I wanted something to go on the final cite, but I also went to the original cite and put what I thought the actual scrape would look like. All of that code can be seen in the jupyter file (commented out). 
    
    Update: I ended up fixing this problem by using splinter. Everything shows up as it is supposed to now.

The only other big problem I had was to the scraped information to show up on the page when you push the button. I got through several errors but I hit a wall with one that had to do with something in MongoDB. All of the code is there, but since I never got the information to show up, the html hasn't been perfected.
    
    Update: When I went to troubleshoot this again, I had to reinstall all the dependencies, and it ended up working. I am not sure what issues it was having before.
    
    Update: I realized that the html that got saved for the initial submission of this assignment wasn't the full page. I had the full page. It just did not get pushed.


Includes: 
1. Mission to Mars Folder

    a. the scraping script called mission_to_mars.ipynb
    
    b. the python file, scrape_mars.py, that took the scrapping from the jupyter file and put them intoa format to be used to create the new page
    
    c. the app.py file that runs the flask app
    
    d. a template folder with the html file for the website
    
    e. a png image of how the cite looks pre-scrape function and post scrape function
