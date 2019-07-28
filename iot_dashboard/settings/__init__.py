from iot_dashboard.env import APP_ENV


if APP_ENV in ('dev', 'prod'):
    exec('from .%s import *' % APP_ENV)
