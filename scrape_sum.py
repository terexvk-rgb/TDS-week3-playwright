import asyncio
import re
from playwright.async_api import async_playwright

seeds = list(range(73, 83))
BASE = "https://sanand0.github.io/tdsdata/js_table/?seed={}"


async def main():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for seed in seeds:
            url = BASE.format(seed)
            await page.goto(url)

            # wait for tables to load
            await page.wait_for_selector("table")

            tables_text = await page.inner_text("table")

            numbers = list(map(int, re.findall(r"-?\d+", tables_text)))
            page_sum = sum(numbers)

            print(f"Seed {seed} sum={page_sum}")

            total_sum += page_sum

        await browser.close()

    # IMPORTANT: exact format for grader
    print(f"TOTAL_SUM={total_sum}")


asyncio.run(main())