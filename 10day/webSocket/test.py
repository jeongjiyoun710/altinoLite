import asyncio

async def test():
    print("function start!")
    await asyncio.sleep(3)
    print("function end!")



async def main():
    await asyncio.gather(

        test(),
        test(),
        test(),
        test(),
        test()

    )


asyncio.run(main())