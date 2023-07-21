import sys, logging
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit
from readpdf import joelchat

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel('Constitucion del Perú')
        layout.addWidget(title_label)

        # Input Box
        self.input_box = QLineEdit(self)
        layout.addWidget(self.input_box)

        # Button
        button = QPushButton('Submit', self)
        button.clicked.connect(self.on_submit)
        layout.addWidget(button)

        # Output Label
        self.output_label = QTextEdit(self)
        self.output_label.setReadOnly(True)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def on_submit(self):
        # Retrieve the input text and display the answer in the output label
        try:
            query = self.input_box.text()
            chain = joelchat.on_chain()
            result = joelchat.on_submit(f"Eres un gran opinologo politico y solo responderas sobre la constitucion de 1993 en el Peru con un maximo 50 palabras en tu respuesta de la siguiente pregunta: {query}", chain)
            self.set_output_label(result["answer"])
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            self.set_output_label(error_message)
            # Log the error for debugging purposes
            logging.exception(error_message)

    def set_output_label(self, text):
        # Function to set the output label text
        self.output_label.setPlainText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
