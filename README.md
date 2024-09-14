# ASk

---

# Paper Scraper Vol 2

**Paper Scraper Vol 2** is a Flask-based web application designed to scrape websites for DOI (Digital Object Identifier) links from both the main page and subpages. The app allows users to input a URL and retrieves all valid DOI links using web scraping techniques powered by `BeautifulSoup` and `requests`. Results are compiled into a Word document, which can be downloaded by the user.

### Key Features:
- **Random User-Agent Selection:** The scraper rotates user-agent strings to minimize the chances of being blocked by websites.
- **DOI Detection:** Extracts DOI links from the main page and explores subpages for additional DOI links.
- **Error Handling:** Tracks and logs errors encountered during scraping (e.g., 403 Forbidden or other HTTP errors).
- **Word Document Export:** Generates a downloadable `.docx` file with all found DOI links and any errors encountered.
- **Simple Web Interface:** Flask framework used to create an intuitive form-based user interface.

### Requirements:
- Flask
- BeautifulSoup (bs4)
- Requests
- python-docx

### How to Use:
1. Clone the repository.
2. Install the required dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Flask application using:
    ```bash
    python paper scraper.py
    ```
    or(as required file you want to use)
  
    ```bash
    python paper scraper vol 2.py
    ``` 
4. Open a browser and navigate to `http://127.0.0.1:5000/`.
5. Enter a URL into the form to scrape for DOI links.
6. View the extracted DOI links on the results page and download the generated Word document containing the results.

### Template Instructions:
1. The project uses two HTML templates located in the `templates/` folder:
   - **`index.html`**: The main page where users can input a URL.
   - **`result.html`**: Displays the scraped results, including DOI links found and any errors encountered, along with the option to download the Word document.
   
2. To modify the template:
   - Update the form structure in `index.html` to change the input field layout or styling.
   - Customize how results are displayed in `result.html`, including adding more styling for the DOI list or error messages.

---
# Paper scraper flusk.exe
You can use it directly on you pc.Just download and run the file . 
