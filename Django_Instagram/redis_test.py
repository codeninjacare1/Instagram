import redis

r = redis.Redis.from_url("rediss://default:AT7lAAIjcDE5YWFiNmUzMDlhMGY0MmJiYTVjODM0MjcxYWY2MTY5OXAxMA@lenient-ferret-16101.upstash.io:6379")
r.set('foo', 'bar')
value = r.get('foo')