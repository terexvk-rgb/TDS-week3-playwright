import asyncio
import re
from playwright.async_api import async_playwright

START_URL = "https://sanand0.github.io/tdsdata/js_table/?seed=73"


async def main():
    total_sum = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(START_URL)

        for _ in range(10):  # seeds 73 → 82
            await page.wait_for_selector("table")

            table_text = await page.inner_text("table")
            numbers = list(map(int, re.findall(r"-?\d+", table_text)))

            page_sum = sum(numbers)
            total_sum += page_sum

            print(f"PAGE_SUM={page_sum}", flush=True)

            next_btn = page.locator("text=Next")
            if await next_btn.count() > 0:
                await next_btn.click()
                await page.wait_for_timeout(1000)

        await browser.close()

    print(f"TOTAL_SUM={total_sum}", flush=True)


asyncio.run(main())