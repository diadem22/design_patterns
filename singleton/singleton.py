class CodeLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CodeLogger, cls).__new__(cls)
            cls._instance.log_file = "application.log"
        return cls._instance

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

logger1 = CodeLogger()
logger1.log("Log entry 1")

logger2 = CodeLogger()
logger2.log("Log entry 2")

print(logger1 is logger2)  