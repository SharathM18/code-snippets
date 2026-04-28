from dataclasses import dataclass
from pathlib import Path

import typer
from loguru import logger

from src.core.config import load_config
from src.core.logger import setup_logging

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "settings.yaml"
SCRIPT_NAME = Path(__file__).stem

app = typer.Typer(help="")


@dataclass
class AppPaths:
    base_output_dir: Path

    @property
    def logs(self) -> Path:
        return self.base_output_dir / "logs"

    @property
    def data(self) -> Path:
        return self.base_output_dir / "data"

    def create_all(self):
        self.base_output_dir.mkdir(parents=True, exist_ok=True)
        self.logs.mkdir(parents=True, exist_ok=True)
        self.data.mkdir(parents=True, exist_ok=True)


def logic(config: dict, cli_args: dict, paths: AppPaths):
    print(f"config: {config}, cli_args:  {cli_args}")
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.success("SUCCESS")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
    print(
        f"out_dic: {paths.base_output_dir}, data_dir: {paths.data}, log_dir: {paths.logs}"
    )


def main(cli_args: dict):
    input_paths = AppPaths(base_output_dir=Path(cli_args["out_dir"]))
    input_paths.create_all()

    config = load_config(config_file=CONFIG_PATH, script_name=SCRIPT_NAME)
    setup_logging(log_dir=input_paths.logs, log_level=cli_args["log_level"])

    logic(config=config, cli_args=cli_args, paths=input_paths)


@app.command(name=SCRIPT_NAME)
def cli_args_collectors(
    # default string "INFO"
    log_level: str = typer.Option(
        "INFO", help="Single string (e.g., --log_level INFO)"
    ),
    # multiple files and required value (...)
    path: Path = typer.Option(
        ..., exists=False, help="Single file path (e.g., --path </some/to/file>)"
    ),
    # multiple files
    paths: list[Path] = typer.Option(
        ...,
        help="Multiple file paths (e.g. --path  </path/to/file> --path  </path/to/file>)",
    ),
    # single directory
    out_dir: Path = typer.Option(
        None, exists=False, help="Single directory (e.g., --out_dir </path/to/dir/> )"
    ),
    # multiple directories and default value is []
    dirs: list[Path] = typer.Option(
        [],
        help="Multiple directories (e.g., -dir </path/to/dir/> --dir </path/to/dir/> )",
    ),
    # boolean
    boolean_value: bool = typer.Option(False, help="Boolean flag"),
    # number
    number_value: int = typer.Option(0, help="Integer value"),
):
    cli_args = {
        "log_level": log_level,
        "path": path,
        "paths": paths,
        "out_dir": out_dir,
        "dirs": dirs,
        "boolean_value": boolean_value,
        "number_value": number_value,
    }
    main(cli_args=cli_args)


if __name__ == "__main__":
    app()
