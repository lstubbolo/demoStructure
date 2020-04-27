#   this file contains all the default settings objects used in the file


MAIN_OBJ = {
            'self': 'mainSettings.json',
            'error': 'True',
            'OCR_Setup': 'False',
            'Audio_Setup': 'False',
            'OCR_Active': 'False',
            'Audio_Active': 'False'
        }

OCR_OBJ = {
            'self': 'ocrSettings.json'

}

AUDIO_OBJ = {
            'self': 'audioSettings.json',
            'refPath': 'reference.wav',
            'smplPath': 'sample.wav',
            'loopMode': 'single',
            'loopEnd': '',
            'detected': 'False',
            'reference': 0,
            'fb_url': 'filler_audio_url'
}

FB_OBJ = {
            'self': 'fbSettings.json',
            'connected': 'False',
            'msg_from_fb': '',
            'msg_to_fb': '',
            'msg_dest_url': ''
}

GUI_OBJ = {
            'self': 'guiSettings.json',
            'stopRequest': 'False',
            'msg_to_GUI': ''
}

LIST_ALL = {
            'mainSettings.json': MAIN_OBJ,
            'ocrSettings.json': OCR_OBJ,
            'audioSettings.json': AUDIO_OBJ,
            'fbSettings.json': FB_OBJ,
            'guiSettings.json': GUI_OBJ,
}

LOOP_TYPES = {}