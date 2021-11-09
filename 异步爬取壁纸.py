import asyncio
import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/2021/1014/20b01474721a82dc822d989d09735324.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/1014/2722023d2be9ef844485a3cddc5aca4f.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/1014/0f006542bfa0623df4cf31e6e599b010.jpg'
]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode='wb') as f:
                f.write(await resp.content.read())
    print(name, "over")


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
