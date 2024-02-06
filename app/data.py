class InputData:
    def __init__(self, url='', p=0, h=0, length_min=10, length_max=100, browser="Chrome"
                 , file_path='', save_path=''):
        self.url = url
        self.p = bool(p)
        self.h = bool(h)
        self.file_path = file_path
        self.length_min = length_min
        self.length_max = length_max
        self.save_path = save_path
        self.browser = browser
