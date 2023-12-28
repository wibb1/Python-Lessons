from datetime import datetime
import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Averspeed Speed Calculator")
        grid = QGridLayout()

        # create widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        ## dropdown for units
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Metric (km)", "Imperial (mi)"])

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # create grid and add widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo_box, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance / time
        unit = 'mph'
        if self.combo_box.currentText() == 'Metric (km)':
            unit = 'kph'
        self.output_label.setText(f"Average speed is {speed} {unit}")


def speed_calculator():
    app = QApplication(sys.argv)
    speed_calculator = SpeedCalculator()
    speed_calculator.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    speed_calculator()
