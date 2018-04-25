import ruamel.yaml
from app import configuration as C


with open(C.INVENTORY, "r") as f:
    yml = ruamel.yaml.YAML(typ="rt", pure=True)
    devices = yml.load(f)
