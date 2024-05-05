from takion_tls import Session

async def main():
    session = Session("chrome_124")
    response = await session.get("https://example.com")
    print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
