from pathlib import Path
import shutil
import uuid


class WorkspaceManager:

    def __init__(self):

        self.base_path = (
            Path.home()
            / "JarvisAI"
            / "workspaces"
        )

        self.base_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def create_workspace(self):

        workspace_id = uuid.uuid4().hex

        workspace_path = (
            self.base_path
            / workspace_id
        )

        workspace_path.mkdir(
            parents=True,
            exist_ok=True
        )

        return {
            "id": workspace_id,
            "path": str(workspace_path)
        }

    def get_workspace(self, workspace_id):

        workspace_path = (
            self.base_path
            / workspace_id
        )

        if not workspace_path.exists():
            raise FileNotFoundError(
                "El workspace solicitado no existe."
            )

        return workspace_path

    def copy_file(
        self,
        source,
        workspace_id
    ):

        source_path = Path(source)

        if not source_path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {source}"
            )

        workspace_path = self.get_workspace(
            workspace_id
        )

        destination = (
            workspace_path
            / source_path.name
        )

        shutil.copy2(
            source_path,
            destination
        )

        return str(destination)

    def list_files(
        self,
        workspace_id
    ):

        workspace_path = self.get_workspace(
            workspace_id
        )

        return [
            str(file.name)
            for file in workspace_path.iterdir()
            if file.is_file()
        ]


workspace_manager = WorkspaceManager()
