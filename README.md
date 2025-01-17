Objective: The aim is to create a web scraper usuing python that pulls all the current new articles and stories from "BBC News" and "Times of India" by extracting all the tags from the HTML of BBC News and Times of India. 

Technology Stack: 
    1. Language: Python
    2. IDE: Pycharm
    3. Tools/Models: BeautifulSoup4

Overview: The project is crafted to extract current articles of the day by BBC News and Times of India, making it easier to gain perspective on the recent news. Both New Sites utilizes tags to generate links to the different websites that comprise its platform. Consequently, along with some supplementary data, you will gather all the URLs of the articles featured on BBC News and Times of India. I am using BeautifulSoup module to examine the articles from BBC News. Parsing involves analyzing a format such as HTML and employing a programming language to organize it. For instance, it can involve converting data into an object.

Key Features:
    1. The primary functionality of the project involves scraping designated websites (BBC News and Time of India) to gather article URLs by searching for terms such as                  "articles" or "news" within the links. 
    2. The project incorporates error handling to address issues like network failures or invalid URLs, ensuring seamless operation without crashes by logging any encountered            errors (e.g., URLError).  
    3. Utilizing Python's logging module enables the tracking and display of the URLs identified during the scraping process. It provides clear and useful feedback, allowing you         to monitor the scraping activities effectively.  
    4. Since the code is developed in Python, it is designed to operate on multiple platforms (Windows, MacOS, Linux) with minimal adjustments required.  
    5. The output is well-structured with messages such as "Fetching BBC News" and "Fetching Time of India News," making it simple to follow the scraping activities for each             site. The logged article URLs include valuable information to identify which URLs were successfully retrieved.  

Benefits:
    1. Error Management: The scraper is now capable of managing errors such as network problems or invalid URLs in a smooth manner.  
    2. Flexibility: It accommodates both absolute and relative URLs, enhancing the scraper's adaptability.  
    3. Performance: The use of modular code simplifies maintenance and expansion.


Conclusion: It is a beginner friendly program structured to stay up-to-date on the ongoing national as well as worldwide affairs.
