"""
sentry_quotas
~~~~~~~~~~~~~

:copyright: (c) 2012 by the Sentry Team, see AUTHORS for more details.
:license: Apache License 2.0, see LICENSE for more details.
"""

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-quotas').version
except Exception, e:
    VERSION = 'unknown'
