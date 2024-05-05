from takion_tls import Session

async def main():
    session = Session()
    session.update_proxy("localhost:3128")
    response = await session.get("https://example.com")
    print(response.text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
