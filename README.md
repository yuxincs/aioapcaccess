# aioapcaccess

[![build](https://github.com/yuxincs/aioapcaccess/actions/workflows/build.yaml/badge.svg)](https://github.com/yuxincs/aioapcaccess/actions/workflows/build.yaml?query=branch%3Amain)
[![codecov](https://codecov.io/github/yuxincs/aioapcaccess/branch/main/graph/badge.svg?token=8zhys5YAk9)](https://codecov.io/github/yuxincs/aioapcaccess)
[![PyPI](https://img.shields.io/pypi/v/aioapcaccess)](https://pypi.org/project/aioapcaccess/)
[![GitHub](https://img.shields.io/github/license/yuxincs/aioapcaccess)](https://github.com/yuxincs/aioapcaccess/blob/main/LICENSE)

An async implementation of [apcaccess](https://linux.die.net/man/8/apcaccess). This
library provides programmatic access to the status information provided by
[apcupsd](http://www.apcupsd.org/) over its Network Information Server (NIS) which
usually listens on TCP port 3551.

This project is a re-implementation of the synchronous version
[flyte/apcaccess](https://github.com/flyte/apcaccess) using
[asyncio](https://docs.python.org/3/library/asyncio.html), where a lot of the logic is
borrowed and improved.

# Install

Install with pip:

```
$ pip install aioapcaccess
```

# Usage

The primary API for getting the status from APCUPS is `aioapcaccess.request_status`.
It returns a `dict` mapping from field names (e.g., "SERIALNO") to
their values in string format. What fields are available will depend on the model of
your APC UPS, see [APCUPSD manual](http://www.apcupsd.org/manual/) for details.

The following example shows a typical usage of `aioapcaccess`

```python
import asyncio
import aioapcaccess

async def main():
    result = await aioapcaccess.request_status(host='localhost', port=3551)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
```

The example above will print the following (prettified and simplified):

```
OrderedDict([
  ('APC', '001,036,0879'),
  ...,
  ('BATTV', '13.7 Volts'),
  ('CUMONBATT', '0 Seconds')
))])
```

In addition to `request_status`, we offer the following functions for advanced uses:

- `aioapcaccess.request_raw_status` for getting raw (unparsed) status in `bytes`.
- `aioapcaccess.parse_raw_status` for parsing the `bytes` to the dict shown above.
- `aioapcaccess.split_unit` for splitting the supported unit suffix from the value
  strings, returning a tuple `(value, unit)`. You can check `aioapcaccess.UNITS` for
  the set of supported units. Note that units are also in the forms of strings
  (e.g., "Seconds", "Volts"). If no valid units are found in the value strings, `unit`
  will be `None`.
