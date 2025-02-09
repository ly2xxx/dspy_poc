import asyncio
from playwright.async_api import async_playwright

async def analyze_webpage():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.betfair.com/betting/football/brazilian-mato-grossense-matches/ce-operario-varzea-grandense-v-primavera-mt/e-34019122")

        # Extract team names
        home_team = await page.text_content('xpath=//div[@class="event__participant event__participant--home"]')
        away_team = await page.text_content('xpath=//div[@class="event__participant event__participant--away"]')

        # Extract match details
        match_details = await page.text_content('xpath=//div[@class="event__title"]')

        # Print the extracted information
        print(f"Home Team: {home_team}")
        print(f"Away Team: {away_team}")
        print(f"Match Details: {match_details}")

        # Close the browser
        await browser.close()

# Run the analysis
asyncio.run(analyze_webpage())