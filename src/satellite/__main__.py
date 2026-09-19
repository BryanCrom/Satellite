import asyncio
import logging

from satellite import *

logger = logging.getLogger("main")

async def main () -> None:
    logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p", level=logging.DEBUG)
    logger.info("started")

    satellite = Satellite(speed=100, altitude=1)

    subject_name = "satellite_01.telemetry"
    nc = await nats_setup()
    await nats_sub(nc, subject_name)

    try:
        while(True):
            await nc.publish(subject_name, satellite.get_telemetry().encode())
            await asyncio.sleep(2)

    except(KeyboardInterrupt):
        await nc.flush()
        await nc.close()

        logger.info("finished")

if __name__ == "__main__":
    asyncio.run(main())