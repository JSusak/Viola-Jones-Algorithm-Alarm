#Every X seconds, send a signal to the main file to get the currently displayed contents in a frame.
#Currently broken, need to work on fixing it!
import asyncio
import time
import sched


async def repeat(interval, func, *args, **kwargs):
    while True:
        await asyncio.gather(
            await func(*args,**kwargs),
            asyncio.sleep(interval)
        )

async def sendSignal():
    await asyncio.sleep(1)
    await print("lol")


async def main():
    imageThread = asyncio.ensure_future(repeat(10,sendSignal()))
    await imageThread
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

s = sched.scheduler(time.time, time.sleep)
def captureFrame(sc): 
    print("Doing stuff...")
    s.enter(10, 1, captureFrame, (sc,))

s.enter(10, 1, captureFrame, (s,))
s.run()
