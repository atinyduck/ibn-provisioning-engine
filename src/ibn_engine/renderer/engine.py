# engine.py
# ==
# ==
# ==

# libraries
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Automatically set the path for templates
TEMPLATES_DIR = Path(__file__).parent / "templates"

def render_device_config(intent_data: dict, template_name: str = "base_config.j2") -> str:
    """Renders vendor-specific CLI commandsfrom validated intent data using Jinja2 templates."""
    vendor_os = intent_data["vendor_os"]
    vendor_template_dir = TEMPLATES_DIR / vendor_os
    
    if not vendor_template_dir.exists():
        raise FileNotFoundError(f"Template directory for vendor '{vendor_os}' no template folder found")
    
    env = Environment(
        loader=FileSystemLoader(str(vendor_template_dir)),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    template = env.get_template(template_name)
    rendered_config = template.render(**intent_data)
    return rendered_config

# end of file