class Logger:
    def info(self, message):
        """Log de informação"""
        print(f"[INFO] {message}")
    
    def error(self, message):
        """Log de erro"""
        print(f"[ERROR] {message}")