class ConsoleNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[УВЕДОМЛЕНИЕ -> {recipient}] {message}")
