# laoder.py
# ==
# ==
# ==

# libraries
import ipaddress
from pathlib import Path
import yaml

def load_and_validate_intent(file_path: str | Path) -> dict:
    """Reads a YAML intent files and validates networking rules."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Intent file not found: {path}")
    
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        
    if not isinstance(data, dict):
        raise ValueError("Intent file must contain a dictionary at the top level.")
    
    # Validate networking rules
    # Validate top-level keys
    required_keys = ['hostname', 'vendor_os']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
        
    # Validate VLAN IDs if present
    for vlan in data.get("vlans", []):
        vlan_id = vlan.get("id")
        if not isinstance(vlan_id, int) or not (1 <= vlan_id <= 4094):
            raise ValueError(f"Invalid VLAN ID: {vlan_id}. Must be an integer between 1 and 4094.")
        
    # Validate OSPC IP addresses if present
    if "ospf" in data:
        ospf = data["ospf"]
        ipaddress.IPv4Address(ospf["router_id"])  # Validate router ID
        
        for net in ospf.get("networks", []):
            ipaddress.IPv4Network(net["ip"])       # Validate network IP address
            ipaddress.IPv4Address(net["wildcard"]) # Validate network wildcard mask
    
    return data