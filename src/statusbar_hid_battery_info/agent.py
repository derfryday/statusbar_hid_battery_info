import logging
import os
from pathlib import Path
from typing import Final
import sys
import subprocess


class LaunchAgent:
    template_file_name: Final[str] = "statusbar_hid_batt_info.plist"
    agent_name: Final[str] = "dev.derfryday.statusbar-hid-batt-info.plist"

    @staticmethod
    def create_launchd_file():
        target_launch_agents_path: Path = Path.home() / "Library/LaunchAgents"
        logging.info("Launch agent will be installed into %s", str(target_launch_agents_path))
        launch_file: Path = target_launch_agents_path / f"{LaunchAgent.agent_name}.plist"
        template_file: Path = Path(__file__).resolve().parent / "resources" / LaunchAgent.template_file_name
        raw_template: str = template_file.read_text(encoding="utf-8")

        executable_path: Path = Path(sys.argv[0]).resolve()
        raw_template = (
            raw_template
            .replace("%AGENT_NAME%", LaunchAgent.agent_name)
            .replace("%PATH_TO_STATUSBAR_EXECUTABLE%", str(executable_path))
        )

        logging.info("Creating Launch Agent file \"%s\".", str(launch_file))
        launch_file.write_text(raw_template, encoding="utf-8")

    @staticmethod
    def delete_launchd_file():
        target_launch_agents_path: Path = Path("~/Library/LaunchAgents").resolve()
        launch_file = target_launch_agents_path / f"{LaunchAgent.agent_name}.plist"
        logging.info("Deleting Launch Agent File \"%s\"", str(launch_file))
        launch_file.unlink(missing_ok=True)

    @staticmethod
    def enable_launchd_service():
        command: str = f"launchctl load -w ~/Library/LaunchAgents/{LaunchAgent.agent_name}.plist"
        logging.info("Loading LaunchAgent with command: %s", command)
        subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def disable_launchd_service():
        command: str = f"launchctl remove {LaunchAgent.agent_name}"
        logging.info("removing LaunchAgent with command: %s", command)
        subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def start_launchd_agent():
        command: str = f"launchctl start {LaunchAgent.agent_name}"
        logging.info("starting LaunchAgent with command: %s", command)
        subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def restart_launchd_agent():
        command: str = f"launchctl kickstart -k gui/{os.getuid()}/{LaunchAgent.agent_name}"
        logging.info("restart LaunchAgent with command: %s", command)
        subprocess.run(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

