from tools.files.inspector import file_inspector
from tools.files.text_tool import text_tool


class ToolManager:

    def inspect(self, file_path):

        return file_inspector.inspect(
            file_path
        )

    def read_file(self, file_path):

        information = (
            file_inspector.inspect(
                file_path
            )
        )

        if not information["valid"]:

            raise FileNotFoundError(
                information["error"]
            )

        file_type = information["type"]

        if file_type in {
            "text",
            "markdown",
            "python",
            "json"
        }:

            return text_tool.read(
                file_path
            )

        raise ValueError(
            "Todavía no existe una herramienta "
            f"de lectura para: {file_type}"
        )

    def create_text_version(
        self,
        file_path,
        content
    ):

        return text_tool.create_version(
            source_path=file_path,
            content=content
        )


tool_manager = ToolManager()
