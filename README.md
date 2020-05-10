faat.pikapool
=============

This package is shamelessly forked from the [pika_pool](https://github.com/bninja/pika-pool) package.

I would have used their package directly, but it doesn't seem to be maintained anymore.

```bash
pip install faat.pikapool
```

and use it:

```python
import json

import pika
import faat.pikapool

params = pika.URLParameters(
    'amqp://guest:guest@localhost:5672/?'
    'socket_timeout=10&'
    'connection_attempts=2'
)

pool = faat.pikapool.QueuedPool(
    create=lambda: pika.BlockingConnection(parameters=params),
    max_size=10,
    max_overflow=10,
    timeout=10,
    recycle=3600,
    stale=45,
)

with pool.acquire() as cxn:
    cxn.channel.basic_publish(
        body=json.dumps({
            'type': 'banana',
            'description': 'they are yellow'
        }),
        exchange='',
        routing_key='fruits',
        properties=pika.BasicProperties(
            content_type='application/json',
            content_encoding='utf-8',
            delivery_mode=2,
        )
    )
```
