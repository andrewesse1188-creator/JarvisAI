from pathlib import Path


class FileInspector:

    SUPPORTED_TYPES = {
        ".txt": "text",
        ".md": "markdown",
        ".py": "python",
        ".json": "json",
        ".csv": "spreadsheet",
        ".xlsx": "spreadsheet",
        ".docx": "document",
        ".pdf": "pdf"
    }

    def inspect(self, file_path):

        path = Path(file_path)

        if not path.exists():

            return {
                "valid": False,
                "error": "El archivo no existe."
            }

        extension = (
            path.suffix.lower()
        )

        file_type = (
            self.SUPPORTED_TYPES.get(
                extension,
                "unknown"
            )
        )

        return {
            "valid": True,
            "name": path.name,
            "extension": extension,
            "type": file_type,
            "size_bytes": path.stat().st_size,
            "supported": (
                extension
                in self.SUPPORTED_TYPES
            )
        }


file_inspector = FileInspector()
