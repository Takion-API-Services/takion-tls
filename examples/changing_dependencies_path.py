from takion_tls import Session

async def main():
    Session.library_path = "./custom_library_path/"
    session = Session("chrome_124")
    response = await session.get("https://example.com")
    print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
