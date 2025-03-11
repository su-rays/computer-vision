class LoggingMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class App(LoggingMixin):
    def run(self):
        self.log("Application started.")

app = App()
app.run()
