"""
MableLink Engine

This is the heart of the application.
Every subsystem is initialized from here.
"""


class Engine:

    def __init__(self):

        self.running = False

    def start(self):

        print("Starting MableLink Engine...")

        self.running = True

        print("Engine Started.")

    def stop(self):

        print("Stopping Engine...")

        self.running = False

        print("Engine Stopped.")