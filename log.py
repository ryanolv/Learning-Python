class LogMixin:      #pode se tornar um método estático
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self,msg):
        self.write(f'ERROR: {msg}')



