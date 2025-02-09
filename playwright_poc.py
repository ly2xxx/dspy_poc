from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Create a browser instance
    browser = p.chromium.launch(headless=False)
    
    # Navigate to the webpage
    page = browser.new_page()
    page.goto("https://www.livescore.com/en/football/england/fa-cup-round-4/blackburn-rovers-vs-wolves/1439491/")
    
    # Parse the HTML content of the webpage
    html = page.content()
    
    # Extract key information from the parsed HTML
    team1_name = page.query_selector("#match-name").text_content().strip()
    team2_name = page.query_selector("#opponent-name").text_content().strip()
    score = page.query_selector(".score").text_content().strip()
    date = page.query_selector("#date").text_content().strip()
    
    # Print the extracted key information
    print(f"Team 1: {team1_name}")
    print(f"Team 2: {team2_name}")
    print(f"Score: {score}")
    print(f"Date: {date}")

# Evaluate to the correct value for answer
answer = f"{team1_name} vs {team2_name}, Score: {score}, Date: {date}"
print(answer)