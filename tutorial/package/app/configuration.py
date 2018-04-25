import os
import ruamel.yaml


with open("configuration.yaml", "r") as f:
    yml = ruamel.yaml.YAML(typ="rt", pure=True)
    _cfg = yml.load(f)


STAGING_USER = _cfg.get('staging_user') or os.environ['ZTP_STAGING_USER']
STAGING_PASS = _cfg.get('staging_pass') or os.environ['ZTP_STAGING_PASS']
TFTP_ROOT = _cfg.get('tftp_root') or os.environ['TFTP_ROOT']
REDIS_URL = _cfg.get('redis_url') or os.environ['REDIS_URL']
INVENTORY = _cfg.get('inventory') or os.environ['ZTP_INVENTORY']
SLACK_TOKEN = _cfg.get('slack_token') or os.environ['SLACK_TOKEN']
TEMPLATE_DIR = _cfg.get('template_dir') or os.environ['ZTP_TEMPLATES']
