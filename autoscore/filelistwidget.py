from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget
from pathlib import Path
from loguru import logger as log
from typing import Callable, List, Optional, Union


class FileListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.file_types: List[str] = [".docx", ".txt", ".prs"]
        self.set_active: Optional[Callable[[bool], None]] = None

    def setActiveCallback(self, func: Callable[[bool], None]):
        """Sets a callback function that is triggered when files are added."""
        self.set_active = func

    def setFileTypes(self, file_types: Union[List[str], tuple[str, ...]]):
        """Sets allowed file types for drag-and-drop, ensuring correct formatting."""
        if not isinstance(file_types, (list, tuple)):
            raise TypeError("file_types parameter requires a list or tuple")

        # Ensure each type starts with a dot and is lowercase
        normalized_types = {atype.lower() if atype.startswith(".") else f".{atype.lower()}" for atype in file_types}
        self.file_types = list(set(self.file_types) | normalized_types)

    def dragEnterEvent(self, event):
        """Handles drag event entry."""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        """Handles drag movement over the widget."""
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Handles file drops into the widget."""
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                path = url.toLocalFile() if url.isLocalFile() else url.toString()
                path_obj = Path(path)
                suffix = path_obj.suffix.lower()

                if path_obj.is_file():
                    if suffix in self.file_types and not self._is_duplicate(path):
                        links.append(str(path_obj.absolute()))
                    else:
                        log.warning(f"Ignored file with unsupported suffix: [{suffix}]")
                elif path_obj.is_dir():
                    # Add directory files matching allowed file types
                    dir_files = [
                        str(file)
                        for file in path_obj.glob("*.*")
                        if file.is_file()
                        and file.suffix.lower() in self.file_types
                        and not self._is_duplicate(str(file.absolute()))
                    ]
                    links.extend(dir_files)

            self.addItems(links)

        else:
            event.ignore()

        if self.set_active:
            self.set_active(self.count() > 0)

    def _is_duplicate(self, file_path: str) -> bool:
        """Checks if a file is already present in the list."""
        return any(self.item(i).text() == file_path for i in range(self.count()))
