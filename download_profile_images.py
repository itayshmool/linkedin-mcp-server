"""One-off script to download LinkedIn profile images using the authenticated browser session."""

import asyncio
import re
from pathlib import Path

from patchright.async_api import async_playwright

PROFILE_DIR = Path.home() / ".linkedin-mcp" / "profile"
OUTPUT_DIR = Path(__file__).parent / "profile_images"

USERNAMES = {
    "stav-iter-737811ab": "Stav Iter Gindi",
}


async def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=True,
            viewport={"width": 1280, "height": 720},
        )
        page = await browser.new_page()

        for username, name in USERNAMES.items():
            print(f"Fetching {name} ({username})...")
            url = f"https://www.linkedin.com/in/{username}/"
            await page.goto(url, wait_until="domcontentloaded")
            await page.wait_for_timeout(3000)

            idx = await page.evaluate(
                """() => {
                    const imgs = document.querySelectorAll('img[src]');
                    for (let i = 0; i < imgs.length; i++) {
                        const src = imgs[i].src || '';
                        if (!src.includes('profile-displayphoto')) continue;
                        // The main profile photo renders at ~128-200px display size
                        const displayW = imgs[i].width || 0;
                        if (displayW >= 100 && displayW <= 300) return i;
                    }
                    return -1;
                }"""
            )

            if idx >= 0:
                img_el = page.locator("img[src]").nth(idx)
                out_path = OUTPUT_DIR / f"{username}.png"
                await img_el.screenshot(path=str(out_path))
                size = out_path.stat().st_size
                print(f"  Saved: {out_path.name} ({size} bytes)")
            else:
                print(f"  No profile image found for {name}")

            await page.wait_for_timeout(2000)

        await browser.close()

    print("\nDone!")


asyncio.run(main())
