import briandais
import hybrid
import conversions
import time

print '--------  Conversions  --------'
bri = briandais.Shakespeare()
print 'Nombre de mots dans l\'arbre de base : ',str(briandais.ComptageMots(bri))


ts = time.clock()
hy = conversions.TransformeBriandaisEnHybride(bri)
te = time.clock()
print 'Conversion briandais -> hybrid en :',1000*(te - ts),' milliseconds'
print 'Nombre de mots dans l\'arbre converti en hybrid : ',str(hybrid.ComptageMots(hy))



ts = time.clock()
bri = conversions.TransformeHybrideEnBriandais(hy)
te = time.clock()
print 'Conversion hybrid ->  briandais en :',1000*(te - ts),' milliseconds'
print 'Nombre de mots dans l\'arbre reconverti en Briandais : ',str(briandais.ComptageMots(bri))