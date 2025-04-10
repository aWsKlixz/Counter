from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QGridLayout, QMainWindow, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

from config import AppConfig
from widgets.timer import TimerWidget

class CounterApp(QMainWindow):

    config: AppConfig

    def _style_button(self, button: QPushButton):
        button.setIconSize(QSize(32, 32))
        button.setFont(QFont("Note Sans", 18))
        button.setMinimumHeight(60)

    def __init__(self, config: AppConfig = AppConfig()):
        super().__init__()
        self.config = config
        self.setWindowIcon(QIcon(str(self.config.assets.icon)))
        self.initUI()


    def initUI(self):
        w, h = self.config.window.width, self.config.window.height
        self.setWindowTitle('Counter App')
        self.setGeometry(100, 100, w, h)
        self.setFixedSize(w, h)

        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        sw = screen_geometry.width()
        sh = screen_geometry.height()
        x = sw - w
        y = sh - h
        self.move(x, y)
        central_widget = QWidget(self)

        main_layout = QHBoxLayout()
        
        counter_frame = QWidget(self)
        counter_layout = QVBoxLayout()
        self.timer_widget = TimerWidget(config=self.config, parent=counter_frame)
        counter_layout.addWidget(self.timer_widget)
        counter_frame.setLayout(counter_layout)
        main_layout.addWidget(counter_frame)

        button_frame = QWidget(self)
        button_layout = QGridLayout()

        self.play_pause_button = QPushButton('Start', counter_frame)
        self.play_pause_button.setIcon(QIcon(str(self.config.assets.Play)))
        self.play_pause_button.clicked.connect(lambda: self.timer_widget.toggle(self.play_pause_button))
        self._style_button(self.play_pause_button)

        self.reset_button = QPushButton('Reset', counter_frame)
        self.reset_button.setIcon(QIcon(str(self.config.assets.Reset)))
        self.reset_button.clicked.connect(lambda: self.timer_widget.reset(self.play_pause_button))
        self._style_button(self.reset_button)

        button_layout.addWidget(self.play_pause_button, 0, 0)
        button_layout.addWidget(self.reset_button, 0, 1)
        button_frame.setLayout(button_layout)
        main_layout.addWidget(button_frame)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)