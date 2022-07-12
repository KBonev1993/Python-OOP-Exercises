class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.app_memory = 0
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False

        self.is_on = True

    def install(self, app, app_memory):
        if app_memory <= self.memory:
            if self.is_on:
                self.memory = self.memory - app_memory
                self.app_memory += app_memory
                self.apps.append(app)
                return f"Installing {app}"

            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self):
        return F"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
