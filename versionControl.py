
####    Pre-functions for main menu buttons that execute before that screen is raised

from OCR_Functions import showImage


def pre_ocr():
    print("Running showImage")

    showImage()

def pre_audio():
    print("Launching Audio Runtime")

def pre_settings():
    print("Launching Main Settings")

def pre_quit():
    print("Launching Quit")

