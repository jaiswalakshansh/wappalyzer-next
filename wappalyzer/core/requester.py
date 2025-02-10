import aiohttp
import asyncio

async def get_response(url, cookie=None, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "deflate",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i",
        "TE": "trailers"
    }
    if cookie:
        headers['Cookie'] = cookie

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(url, **kwargs) as response:
                return await response.text()
        except aiohttp.ClientError as e:
            print(e)
            return None