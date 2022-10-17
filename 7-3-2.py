import asyncio
from pyppeteer import launch

width, heigh = 1366, 768


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'heigh': heigh})
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
