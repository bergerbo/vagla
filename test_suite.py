import briandais
import hybrid
import conversions


bri = briandais.ExampleBase()
liste = briandais.ListeMots(bri)
print liste

hy = conversions.TransformeBriandaisEnHybride(bri)
liste = hybrid.ListerMots(hy)
print liste

bri = conversions.TransformeHybrideEnBriandais(hy)
liste = briandais.ListeMots(bri)
print liste