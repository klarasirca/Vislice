import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')
    #morajo biti v views mapici

@bottle.get('/img/<ime>')
def slike(ime):
    return bottle.static_file(ime, root = 'img')


@bottle.get('/igra/')
def nova_igra():
        id = vislice.nova_igra()
        bottle.redirect('/igra{0}/'.format(id))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre(id_igre)
    return bottle.template('igra.html', id_igre = id_igre , igra=igra, stanje = stanje)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra{0}/'.format(id_igre))


    bottle.run(reloader = True, debug = True)