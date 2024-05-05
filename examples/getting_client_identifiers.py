from takion_tls import Session

async def main():
    session = Session()
    print("Available Client Profiles:", session.clients.profiles)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
