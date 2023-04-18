from PyQt6 import QtWidgets

from window.admin_window import Ui_admin_window
from window.main_window import Ui_MainWindow
# if __name__ == "__main__":
#     import sys

#     app = QtWidgets.QApplication(sys.argv)
#     admin_window = QtWidgets.QDialog()
#     ui = Ui_admin_window(admin_window)
#     admin_window.show()
#     sys.exit(app.exec())

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    admin_window = QtWidgets.QDialog()
    admin = Ui_admin_window(admin_window)
    MainWindow = QtWidgets.QMainWindow()
    main = Ui_MainWindow(MainWindow,admin_window)
    MainWindow.show()
    sys.exit(app.exec())