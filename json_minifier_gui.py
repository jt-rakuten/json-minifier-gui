import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class JSONMinifierApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('JSON Minifier')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.selectButton = QPushButton('Select JSON File', self)
        self.selectButton.clicked.connect(self.selectFile)
        layout.addWidget(self.selectButton)

        self.resultText = QTextEdit(self)
        self.resultText.setReadOnly(True)
        layout.addWidget(self.resultText)

        self.copyLabel = QLabel('Copy the above text for use in Postman mock creation.', self)
        layout.addWidget(self.copyLabel)

        # Create a horizontal layout for the bottom right link
        bottomLayout = QHBoxLayout()
        bottomLayout.addStretch(1)  # Add a stretchable space to push the link to the right

        # Create a QLabel with a hyperlink
        self.docLink = QLabel('<a href="https://github.com/jt-rakuten/json-minifier-gui">Documentation link to the README</a>', self)
        self.docLink.setOpenExternalLinks(True)
        bottomLayout.addWidget(self.docLink)

        layout.addLayout(bottomLayout)

        self.setLayout(layout)

    def selectFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open JSON file', '', 'JSON files (*.json)')
        if fname:
            try:
                with open(fname, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Minify JSON with ensure_ascii=False to retain original characters
                minified = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
                
                # Convert to JSON string format for Postman
                postman_string = json.dumps(minified, ensure_ascii=False)
                
                self.resultText.setPlainText(postman_string)
                
                # Save minified JSON
                output_file = f"{fname.rsplit('.', 1)[0]}_minified.json"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(minified)
                
                self.copyLabel.setText(f'Minified JSON saved to {output_file}\nCopy the above text for use in Postman mock creation.')
            
            except json.JSONDecodeError:
                self.resultText.setPlainText("Invalid JSON file")
            except IOError:
                self.resultText.setPlainText("Error reading or writing file")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JSONMinifierApp()
    ex.show()
    sys.exit(app.exec_())
