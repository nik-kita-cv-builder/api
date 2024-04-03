from dotenv import dotenv_values, get_key


_config_source = get_key('CONFIG_SOURCE', '.env')
config = dotenv_values(_config_source)
