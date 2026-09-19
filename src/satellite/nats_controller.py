import logging
import nats

logger = logging.getLogger("nats")
NATS_URL = "nats://localhost:4222"

async def nats_setup():
    async def disconnect_callback():
        logger.info("disconnected")

    async def reconnect_callback():
        logger.info(f"reconnected to {NATS_URL}")

    async def error_callback(error):
        logger.error(f"Error: {error}")

    async def closed_callback():
        logger.info("connection has been closed")

    return await nats.connect(NATS_URL, error_cb=error_callback, disconnected_cb=disconnect_callback, closed_cb=closed_callback, reconnected_cb=reconnect_callback)

async def nats_sub(nc, subject_name):
    async def msg_handler(msg):
        logger.info(f"{msg.subject}: {msg.data.decode()}")

    await nc.subscribe(subject_name, cb=msg_handler)