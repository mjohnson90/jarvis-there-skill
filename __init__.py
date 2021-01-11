from mycroft import MycroftSkill, intent_file_handler


class JarvisThere(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('there.jarvis.intent')
    def handle_there_jarvis(self, message):
        self.speak_dialog('there.jarvis')


def create_skill():
    return JarvisThere()

