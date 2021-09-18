import platform
from os.path import expanduser

from PySide6 import QtWidgets
from src.Controller.PathHandler import resource_path


class CSV2ClinicalDataSROptions(QtWidgets.QWidget):
    """
    DVH2CSV options for batch processing.
    """

    def __init__(self):
        """
        Initialise the class
        """
        QtWidgets.QWidget.__init__(self)

        # Create the main layout
        self.main_layout = QtWidgets.QVBoxLayout()

        # Get the stylesheet
        if platform.system() == 'Darwin':
            self.stylesheet_path = "res/stylesheet.qss"
        else:
            self.stylesheet_path = "res/stylesheet-win-linux.qss"
        self.stylesheet = open(resource_path(self.stylesheet_path)).read()

        label = QtWidgets.QLabel("Please choose the file location:")
        label.setStyleSheet(self.stylesheet)

        self.directory_layout = QtWidgets.QFormLayout()

        # Directory text box
        self.directory_input = QtWidgets.QLineEdit("No file selected")
        self.directory_input.setStyleSheet(self.stylesheet)
        self.directory_input.setEnabled(False)

        # Change button
        self.change_button = QtWidgets.QPushButton("Change")
        self.change_button.setMaximumWidth(100)
        self.change_button.clicked.connect(self.show_file_browser)
        self.change_button.setObjectName("NormalButton")
        self.change_button.setStyleSheet(self.stylesheet)

        self.directory_layout.addWidget(label)
        self.directory_layout.addRow(self.directory_input)
        self.directory_layout.addRow(self.change_button)

        self.main_layout.addLayout(self.directory_layout)
        self.setLayout(self.main_layout)

    def set_csv_input_location(self, path, enable=True,
                               change_if_modified=False):
        """
        Set the location for the input CSV file for ClinicalData2DICOM-SR.
        :param path: desired path.
        :param enable: Enable the directory text bar.
        :param change_if_modified: Change the directory if already been
                                   changed.
        """
        if not self.directory_input.isEnabled():
            self.directory_input.setText(path)
            self.directory_input.setEnabled(enable)
        elif change_if_modified:
            self.directory_input.setText(path)
            self.directory_input.setEnabled(enable)

    def get_csv_input_location(self):
        """
        Get the location of the desired input directory.
        """
        return self.directory_input.text()

    def show_file_browser(self):
        """
        Show the file browser for selecting a file for the input CSV.
        """
        # Open a file dialog and return chosen directory
        csv_path = QtWidgets.QFileDialog.getOpenFileName(
            None, "Open Clinical Data File", "", "CSV data files (*.csv)"
        )[0]

        # Update file path
        self.set_csv_input_location(csv_path, change_if_modified=True)
