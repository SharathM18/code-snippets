class Notification:
    def __init__(
        self,
        config,
        logger,
    ):
        self.config = config
        self.logger = logger

    def send_email(self, subject, body):
        if self.config.get("env", "dev"):
            self.logger.info("Sending email notification...")
            print(f"Subject :{subject}")
            print(f"Body :{body}")
        else:
            self.logger.debug("Email notifications disabled")
