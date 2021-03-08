from lxml import etree

def listar (datos):
    nombre=datos.xpath("/tv/channel/@id")
    return nombre

def contar (datos):
    lista1=datos.xpath("/tv/programme[category='Sports']//title/text()")
    return lista1

def buscar (datos, canal):
   busqueda=datos.xpath("/tv/programme[@channel='%s']//title/text()"%canal)
   return busqueda

def informacion (datos, programa):
    info=datos.xpath("/tv/programme[title='%s']//@channel"%programa)
    return info

def libre (datos,idioma):
    var2=datos.xpath("/tv/programme/title[@lang='%s']/text()"%idioma)
    return var2