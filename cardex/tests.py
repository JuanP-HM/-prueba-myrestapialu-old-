from django.test import TestCase
from cardex import models
from django.core.files.images import ImageFile

class TestSignal(TestCase) :
    def test_filtro_es_generado_al_guardar(self):
        print('Test mia')
        with open("cardex/fixtures/my-image.jpg", "rb") as
            alumno = models.Alumno(
                nombre = "Filtro",
                no_control = "11111",
                carrera = "Infor",
                foto = ImageFile(f, name="mi.jpg"),
            )
            #with self. assertLogs ("cardex", level="INFO") as 
            alumno.save()
        #self. assertGreaterEqual (len (cm. output), 1) 
        alumno.refresh_from_db()
        with open(
            "cardex/fixtures/my-image.jpg",
            "rb",
        ) as f:
            expected_content = f.read()
            assert alumno.foto.read() != expected_content
        alumno.foto.delete(save=False)

# Create your tests here.
