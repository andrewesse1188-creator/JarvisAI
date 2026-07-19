from pathlib import Path


class TextTool:

    ALLOWED_EXTENSIONS = {
        ".txt",
        ".md",
        ".py",
        ".json"
    }

    def _validate(self, file_path):

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {file_path}"
            )

        if path.suffix.lower() not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Tipo de archivo no permitido: {path.suffix}"
            )

        return path

    def read(self, file_path):

        path = self._validate(file_path)

        return path.read_text(
            encoding="utf-8"
        )

    def write(
        self,
        file_path,
        content
    ):

        path = Path(file_path)

        if path.suffix.lower() not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Tipo de archivo no permitido: {path.suffix}"
            )

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return str(path)

    def create_version(
        self,
        source_path,
        content
    ):

        source = self._validate(
            source_path
        )

        new_path = source.with_name(
            f"{source.stem}_edited"
            f"{source.suffix}"
        )

        new_path.write_text(
            content,
            encoding="utf-8"
        )

        return str(new_path)


text_tool = TextTool()
