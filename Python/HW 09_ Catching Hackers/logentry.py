class LogEntry:
    def __init__(self, time, ip, success):
        self.time = time
        self.ip = ip
        self.success = success

    @staticmethod
    def fromstring(string):
        time, ip, success = string[1:-1].split('][')
        if success not in ['SUCCESS', 'FAIL']:
            raise ValueError("Only 'SUCCESS' and 'FAIL' are valid values.")
        return LogEntry(float(time), ip, success)

    def __str__(self):
        return "".join(['[', str(self.time), ']','[', str(self.ip), ']','[', str(self.success), ']'])
