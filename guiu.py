import sys, logging
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, \
QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit
from readpdf import joelchat

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("frontend.ui",self)
        self.init_ui()

    def init_ui(self):
        # Button
        self.button.clicked.connect(self.on_submit)

        # Output Label
        self.output_label.setReadOnly(True)

    def on_submit(self):
        # Retrieve the input text and display the answer in the output label
        try:
            query = self.input_box.toPlainText()
            chain = joelchat.on_chain()
            result = joelchat.on_submit(f"Eres un gran opinologo politico y solo \
                                        responderas sobre la constitucion de 1993 \
                                        en el Peru con un maximo 50 palabras en tu \
                                        respuesta de la siguiente pregunta: {query}", chain)
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
