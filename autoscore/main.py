from PySide6.QtCore import QCoreApplication, QSize
from PySide6.QtGui import QIcon

from PySide6.QtWidgets import QApplication

import sys

from autoscore.mainwindow import MainWin
from autoscore.resource import get_resource


def main():
    # Create the application instance
    app = QApplication(sys.argv)

    # Dictate app final close behavior
    app.setQuitOnLastWindowClosed(True)

    # Load application icons
    icon = QIcon()
    icon.addFile(get_resource("icons", "16.png"), QSize(16, 16))
    icon.addFile(get_resource("icons", "24.png"), QSize(24, 24))
    icon.addFile(get_resource("icons", "32.png"), QSize(32, 32))
    icon.addFile(get_resource("icons", "48.png"), QSize(48, 48))
    icon.addFile(get_resource("icons", "64.png"), QSize(64, 64))
    icon.addFile(get_resource("icons", "128.png"), QSize(128, 128))
    icon.addFile(get_resource("icons", "256.png"), QSize(256, 256))  # Primary icon for most cases
    icon.addFile(get_resource("icons", "512.png"), QSize(512, 512))

    app.setWindowIcon(icon)

    # Initialize QSettings once so we can use the default constructor throughout the project
    QCoreApplication.setOrganizationName("TravisSeymour")
    QCoreApplication.setOrganizationDomain("travisseymour.com")
    QCoreApplication.setApplicationName("autocoder")

    # Initialize main window
    main_win = MainWin()
    main_win.setWindowIcon(icon)

    # Show main window
    main_win.show()

    # Execute application event loop
    exit_code = app.exec()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
