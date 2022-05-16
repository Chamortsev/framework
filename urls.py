from views import Index, Info, About, Contacts

routes = {
    '/': Index(),
    '/info/': Info(),
    '/about/': About(),
    '/contacts/': Contacts(),
}
