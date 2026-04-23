from pathlib import Path

import typer
from loguru import logger
from src.scripts.script_one.main import run as run_script_one
from src.scripts.script_two.main import run as run_script_two
from src.shared.config import load_config

PROJECT_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = PROJECT_ROOT / "config.toml"


app = typer.Typer(
    name="automate",
    help="Automation Suite — run any script via sub-commands.",
    no_args_is_help=True,
)


@app.command()
def script_one(
    # REQUIRED VALUE (...)
    env: str = typer.Option(..., help="Environment (dev/stage/prod)"),
    # REQUIRED VALUE (...)
    path: Path | None = typer.Option(..., exists=False, help="Single file path"),
    # logging & default = "INFO"
    log_level: str = typer.Option("INFO", help="Log level"),
    # multiple files
    paths: list[Path] = typer.Option([], help="Multiple file paths"),
    # single directory
    dir: Path | None = typer.Option(None, exists=False, help="Single directory"),
    # multiple directories
    dirs: list[Path] = typer.Option([], help="Multiple directories"),
    # boolean
    boolean_value: bool = typer.Option(False, help="Boolean flag"),
    # number
    number_value: int = typer.Option(0, help="Integer value"),
):
    logger.info("")
    config = load_config(CONFIG_PATH, env)
    cli_args = {
        "path": path,
        "paths": paths,
        "dir": dir,
        "dirs": dirs,
        "boolean_value": boolean_value,
        "number_value": number_value,
        "log_level": log_level,
    }
    run_script_one(config, cli_args)
    logger.info("")


@app.command()
def script_two(
    env: str = typer.Option("dev", help="Environment"),
    dry_run: bool = typer.Option(False, help="Dry run mode"),
):
    config = load_config(CONFIG_PATH, env)
    cli_args = {
        "env": env,
        "dry_run": dry_run,
    }
    run_script_two(config, cli_args)


if __name__ == "__main__":
    app()
