class Logger:
    def info(self, message):
        """Log de informação"""
        print(f"[INFO] {message}")
        print(f"[INFO][ENVIRONMENT] env=" {os.getenv('ENV')})
    
    def error(self, message):
        """Log de erro"""
        print(f"[ERROR] {message}")