import argparse

import tomllib
from services.logging import LoggerService
from services.notification import Notification


def parse_cli_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Automation Script",
        # formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python main.py --env dev
        """,
    )

    parser.add_argument(
        "--env",
        type=str,
        required=True,
        choices=["dev", "staging", "prod"],
        help="Environment to run (dev, staging, prod)",
    )

    parser.add_argument(
        "--path",
        type=str,
        nargs="+",  # This makes it accept one or more values as a list
        required=False,
        default=[],
        help="One or more file/directory paths (space separated)",
    )

    return parser.parse_args()


def load_config(env):
    """Load configuration from TOML file"""
    config_path = "config.toml"

    with open(config_path, "rb") as f:
        full_config = tomllib.load(f)  # Dict output

    # Start with default config
    config = full_config.get("default", {}).copy()

    # Override with environment config
    env_config = full_config.get(env, {})
    config.update(env_config)  # default + env specific config

    # Add environment name to config
    config["environment"] = env

    return config


def usage_example(config, args, logger):
    logger.debug(f"Starting automation in {args.env} environment")
    logger.info(f"Starting automation in {args.env} environment")
    logger.warning(f"Starting automation in {args.env} environment")
    logger.error(f"Starting automation in {args.env} environment")
    print(f"config: {config}")
    print(f"args: {args.env}")
    return True


def logic(logger, notification):
    logger.info("Executing second logic")

    # Send success notification
    notification.send_email(
        subject="Task Complete", body="All tasks processed successfully"
    )

    called_by_other()

    return True


def called_by_other():
    print("This function called by other function")


def main():
    # CLI arguments
    args = parse_cli_args()
    print(f"Running with environment: {args.env}")

    # Load configuration based on environment
    config = load_config(args.env)
    print(config["database"])
    print(args.path)

    # Initialize service
    logger = LoggerService(config["log_level"], "./outs/logs/")
    notification = Notification(config, logger)

    # Calling main logics functions
    usage_example(config, args, logger)
    logic(logger, notification)  # Pass the notification services as args

    logger.info("Automation completed successfully")


if __name__ == "__main__":
    main()
