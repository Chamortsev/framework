from templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', render('about.html')


class Info:
    def __call__(self):
        return '200 OK', 'info'


class Contacts:
    def __call__(self):
        return '200 OK', 'Contacts'
