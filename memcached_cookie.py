""" Беседуем с одним и тем же компьютером """

import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
c = db.get('marco')
print(c)

