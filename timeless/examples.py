from h2time import H2Time, H2Request
import logging
import string
import asyncio

import random

ua = 'h2time/0.1'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('h2time')


async def run_two_gets():
    r1 = H2Request('GET', 'https://tom.vg/?1', {'user-agent': ua})
    r2 = H2Request('GET', 'https://tom.vg/?2', {'user-agent': ua})
    logger.info('Starting h2time with 2 GET requests')
    async with H2Time(r1, r2, num_request_pairs=5) as h2t:
        results = await h2t.run_attack()
        print('\n'.join(map(lambda x: ','.join(map(str, x)), results)))
    logger.info('h2time with 2 GET requests finished')
	
async def run_two_unsafe_gets_localhost():
    r1 = H2Request('GET', 'https://127.0.0.1/try?code=1234512345123451234512345123451234512345')
    r2 = H2Request('GET', 'https://127.0.0.1/try?code=9456794567945679456794567945679456794567')
    logger.info('Starting h2time with 2 GET requests')
    async with H2Time(r1, r2, num_request_pairs=50, num_padding_params=100) as h2t:
        results = await h2t.run_attack()
        print('1st unsafe request arrived first:' + str(count(results, lambda x: x > 0)))
        print('2nd unsafe request arrived first:' + str(count(results, lambda x: x < 0)))
        print('equal:' + str(count(results, lambda x: x == 0)))

async def run_two_safe_gets_localhost():
    r1 = H2Request('GET', 'https://127.0.0.1/trysafe?code=1234512345123451234512345123451234512345')
    r2 = H2Request('GET', 'https://127.0.0.1/trysafe?code=9456794567945679456794567945679456794567')
    logger.info('Starting h2time with 2 GET requests')
    async with H2Time(r1, r2, num_request_pairs=50, num_padding_params=100) as h2t:
        results = await h2t.run_attack()
        print('1st safe request arrived first:' + str(count(results, lambda x: x > 0)))
        print('2nd safe request arrived first:' + str(count(results, lambda x: x < 0)))
        print('equal:' + str(count(results, lambda x: x == 0)))

def count(tuples, op):
    i = 0
    for tuple in tuples:
      if op(tuple[0]): i=i+1
    return i

async def run_two_gets_customize_order():
    r1 = H2Request('GET', 'https://tom.vg/?1', {'user-agent': ua})
    r2 = H2Request('GET', 'https://tom.vg/?2', {'user-agent': ua})
    logger.info('Starting h2time with 2 GET requests')
    async with H2Time(r1, r2, send_order_pattern="12211", num_request_pairs=5) as h2t:
        results = await h2t.run_attack()
        print('\n'.join(map(lambda x: ','.join(map(str, x)), results)))
    logger.info('h2time with 2 GET requests finished')

async def run_two_gets_always_send_r1_first():
    r1 = H2Request('GET', 'https://tom.vg/?1', {'user-agent': ua})
    r2 = H2Request('GET', 'https://tom.vg/?2', {'user-agent': ua})
    logger.info('Starting h2time with 2 GET requests')
    async with H2Time(r1, r2, send_order_pattern="1", num_request_pairs=5) as h2t:
        results = await h2t.run_attack()
        print('\n'.join(map(lambda x: ','.join(map(str, x)), results)))
    logger.info('h2time with 2 GET requests finished')

async def run_two_posts():
    post_data = 'x=' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=2000))
    r1 = H2Request('POST', 'https://tom.vg/post?1', {'user-agent': ua, 'content-length': str(len(post_data)),
                                                     'Content-Type': 'application/x-www-form-urlencoded'}, post_data)
    r2 = H2Request('POST', 'https://tom.vg/post?2', {'user-agent': ua, 'content-length': str(len(post_data)),
                                                     'Content-Type': 'application/x-www-form-urlencoded'}, post_data)
    logger.info('Starting h2time with 2 POST requests')
    async with H2Time(r1, r2, sequential=True, num_request_pairs=2, num_padding_params=30) as h2t:
        results = await h2t.run_attack()
        print('\n'.join(map(lambda x: ','.join(map(str, x)), results)))
    logger.info('h2time with 2 POST requests finished')


async def run_two_gets_loop():
    r1 = H2Request('GET', 'https://tom.vg/?1', {'user-agent': ua})
    r2 = H2Request('GET', 'https://tom.vg/?2', {'user-agent': ua})
    logger.info('Starting h2time with 2 GET requests (loop)')
    for _ in range(3):
        async with H2Time(r1, r2, num_request_pairs=5, sequential=True, inter_request_time_ms=100) as h2t:
            results = await h2t.run_attack()
            print('Got %d results' % len(results))
    logger.info('h2time in loop with 2 GET requests finished')


loop = asyncio.get_event_loop()
loop.run_until_complete(run_two_unsafe_gets_localhost())
loop.run_until_complete(run_two_safe_gets_localhost())
"""
loop.run_until_complete(run_two_gets())
loop.run_until_complete(run_two_gets_customize_order())
loop.run_until_complete(run_two_gets_always_send_r1_first())
loop.run_until_complete(run_two_posts())
loop.run_until_complete(run_two_gets_loop())
"""
loop.close()
