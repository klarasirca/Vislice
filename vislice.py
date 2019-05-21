import bottle
import model

vislice = model.Vislice()
id = vislice.nova_igra()
igra, stanje = vislice.igre[id]

@bottle.get('/')
def index():
    return bottle.template('index.tpl')
    #morajo biti v views mapici

@bottle.get('/igra/')
def testigra():
    return bottle.template('igra.html', id_igra = id, igra=igra, stanje = stanje)
    #morajo biti v views mapici

@bottle.get('/img/<ime>')
def slike(ime):
    return bottle.static_file(ime, root = 'img')

bottle.run(reloader = True, debug = True)

