import asyncio
import logging

import nats

from satellite import Satellite

logger = logging.getLogger("main")
NATS_URL = "nats://localhost:4222"

async def main ():
    logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p", level=logging.DEBUG)
    logger.info("started")

    satellite = Satellite(speed=100, altitude=1)
    logger.info(satellite.get_telemetry())
    await asyncio.sleep(1)

    nc = await nats.connect(NATS_URL)
    subject_name = "satellite_01.telemetry"

    sub = await nc.subscribe(subject_name)
    await nc.publish(subject_name, satellite.get_telemetry().encode())
    msg = await sub.next_msg()
    subject = msg.subject
    telemetry = str(msg.data)[4:-1]
    print(f"{subject}: {telemetry}")

    await nc.flush()
    await nc.close()

    logger.info("finished")

if __name__ == "__main__":
    asyncio.run(main())