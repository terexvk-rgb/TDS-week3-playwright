import asyncio
import re
from playwright.async_api import async_playwright

seeds = list(range(73, 83))

BASE = "https://sanand0.github.io/tdsdata/playwright_seed_{}.html"


async def main():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in seeds:
            url = BASE.format(seed)
            await page.goto(url)

            tables_text = await page.inner_text("body")

            numbers = list(map(int, re.findall(r"-?\d+", tables_text)))
            page_sum = sum(numbers)

            print(f"Seed {seed} sum = {page_sum}")

            total_sum += page_sum

        await browser.close()

    print("FINAL_TOTAL =", total_sum)


asyncio.run(main())