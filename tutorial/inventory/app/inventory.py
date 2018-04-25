import ruamel.yaml

inventory_file = '/opt/ztp/devices.yaml'
inventory_file = '/vagrant/tutorial/inventory/devices.yaml'

with open(inventory_file, "r") as f:
    yml = ruamel.yaml.YAML(typ="rt", pure=True)
    devices = yml.load(f)
