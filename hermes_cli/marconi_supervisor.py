from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

DEFAULT_WORKSPACE = Path("/workspace/autoresearch")
DEFAULT_TMUX_SCRIPT = "marconi_supervisor_tmux.sh"
DEFAULT_RESULTS = "results.tsv"
DEFAULT_BASELINES = "baselines.tsv"


def _workspace_from_args(args) -> Path:
    value = getattr(args, "workspace", None) or os.environ.get(
        "HERMES_MARCONI_WORKSPACE", str(DEFAULT_WORKSPACE)
    )
    return Path(value).expanduser().resolve()


def _tmux_script(workspace: Path) -> Path:
    return workspace / DEFAULT_TMUX_SCRIPT


def _require_workspace(workspace: Path) -> None:
    required = [
        workspace,
        workspace / "README.md",
        workspace / "program.md",
        workspace / "context.md",
        workspace / "AGENTS.md",
        workspace / DEFAULT_TMUX_SCRIPT,
        workspace / "run_marconi_batch.sh",
        workspace / "supervise_marconi_batches.sh",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("✗ Marconi workspace is not ready. Missing:")
        for item in missing:
            print(f"  - {item}")
        sys.exit(1)


def _run(script: Path, action: str, *, check: bool = True, replace_process: bool = False) -> int:
    cmd = [str(script), action]
    if replace_process:
        os.execv(cmd[0], cmd)
    proc = subprocess.run(cmd)
    if check and proc.returncode != 0:
        sys.exit(proc.returncode)
    return proc.returncode


def marconi_command(args) -> None:
    workspace = _workspace_from_args(args)
    _require_workspace(workspace)
    script = _tmux_script(workspace)
    action = getattr(args, "marconi_action", None) or "status"

    if action == "paths":
        print(f"workspace: {workspace}")
        print(f"tmux_control: {script}")
        print(f"results_tsv: {workspace / DEFAULT_RESULTS}")
        print(f"baselines_tsv: {workspace / DEFAULT_BASELINES}")
        return

    if action == "attach":
        _run(script, "attach", replace_process=True)
        return

    _run(script, action)
