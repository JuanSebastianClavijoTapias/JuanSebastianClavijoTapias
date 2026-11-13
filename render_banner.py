import asyncio, os
from playwright.async_api import async_playwright

async def main():
    src = "file://" + os.path.expanduser("~/github_perfil/banner.html")
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1280,"height":340}, device_scale_factor=2)
        await pg.goto(src)
        await pg.wait_for_timeout(1200)
        await pg.screenshot(path=os.path.expanduser("~/github_perfil/assets/banner.png"),
                            clip={"x":0,"y":0,"width":1280,"height":340})
        await b.close()
    print("ok")

asyncio.run(main())
