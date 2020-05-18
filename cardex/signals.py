from django.dispatch import receiver
from .models import Alumno

THUMBNAIL_SIZE = (300, 300)

#logger = logging.getLogger(__name__)

#@receiver(pre_save, sender=Alumno)
def generate_thumbnail(sender, instance, **kwargs):
    #logger.info("Creando filtro y thumbnail para el alumno $d", instance. id,)
    print('hola');
    imagen = Image.open(instance.foto)
    imagen = imagen.filter(ImageFilter.CONTOUR)
    imagen.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    temp_thumb = BytesIO()
    imagen.save(temp_thumb, "JPEG")
    temp_thumb.seek(0)
    instance.foto.save(instance.foto.name,ContentFile(temp_thumb.read()),save=False,)
    temp_thumb.close()