
<?php
// imprime el nombre de usuario que tiene control del proceso php/httpd activo
// (en un sistema con el ejecutable "whoami" disponible en la ruta)
echo exec('pipenv shell');
echo exec('cd myrestapi');
echo exec('manage.py runserver');
?>
