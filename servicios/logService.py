import datetime
from datetime import datetime

class LogService:

    def __init__(self):
        self.log_file = "log.txt"


    def logger(self, metodo_nombre):
        with open(self.log_file, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {metodo_nombre}\n")