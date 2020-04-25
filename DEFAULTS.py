#   this file contains all the default settings objects used in the file


MAIN_OBJ = {
            'self': 'mainSettings.json',
            'fireBaseURL': 'empty',
            'fireBaseInput': 'empty',
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
            'refPath': 'reference.WAV',
            'smplPath': 'sample.WAV',
            'loopMode': 'infinite',
            'loopEnd': '',
            'detected': False,
            'reference': 0
}

LIST_ALL = {
            'mainSettings.json' : MAIN_OBJ,
            'ocrSettings.json' : OCR_OBJ,
            'audioSettings.json' : AUDIO_OBJ
}
