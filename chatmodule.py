from datetime import datetime
import json

class Message:

    def get_current_time(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def __write_to_file(self, message):
        file = open("messages.txt", "a")
        file.write(message.__str__() + "\n")
        file.close
    
    def __read_from_file(self):
        messages = []
        file = open("messages.txt", "r")
        for line in file:
            line = line.replace("\'", "\"")
            msg = dict(json.loads(line[:-1]))
            messages.append(msg)
        file.close()
        return messages


    def send(self, text, sender_name):
        message = dict()
        message["time"] = self.get_current_time()
        message["sender"] = sender_name
        message["message"] = text
        self.__write_to_file(message)
        del message
    
    def receive(self):
        return self.__read_from_file()
    