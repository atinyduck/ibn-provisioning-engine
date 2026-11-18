# cli.py
# ==
# ==
# ==

# libraries
from ibn_engine.parser.loader import load_and_validate_intent
from ibn_engine.renderer.engine import render_device_config


def main():
    intent_path = "examples/intents/campus_ospf.yaml"
    
    print(f"[1/2] Parsing and validating intent file: {intent_path}...")
    intent_data = load_and_validate_intent(intent_path)
    
    print(f"[2/2] Rendering CLI commands for OS: {intent_data['vendor_os']}...\n")
    cli_config = render_device_config(intent_data)
    
    print(cli_config)


if __name__ == "__main__":
    main()