from satellite import Satellite

import asyncio
import logging

logger = logging.getLogger("main")

async def main ():
    logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p", level=logging.DEBUG)
    logger.info("started")
    satellite = Satellite(speed=100, altitude=1)
    satellite.display_info()
    await asyncio.sleep(5)
    satellite.display_info()
    logger.info("finished")

if __name__ == "__main__":
    asyncio.run(main())