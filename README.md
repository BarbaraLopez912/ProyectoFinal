# BeyondGames

Una aplicación Django tipo blog que permite compartir opiniones sobre distintos videojuegos que han encantado al público. Aquellos apasionados por los videojuegos más populares pueden crear una cuenta en nuestra página para no perderse ninguna Actualización.

## Creadores

Bárbara López Betancourt y Manuel Figueroa Flores, dos programadores chilenos comprometidos con este proyecto. Bárbara comenzó creando el proyecto django en sus inicios, organizando carpetas y realizando los ajustes correspondientes. Además realizó las vistas respectivas al manejo de las cuentas (login, logout, registro de usuarios), y posteriormente se encargó de la creación del CRUD para cada publicación. Manuel por otro lado, creó la lógica de las publicaciones: modelos y vistas respectivas, además de darle formato a los formularios correspondientes. Lo anterior en esencia, dado que se apoyaron mutuamente en la corrección de errores y solución de problemas que fueron surgiendo. 

## Requisitos

- Python 3.11
- Django

## Instalación

- Clona el repositorio: 'git clone https://github.com/BarbaraLopez912/ProyectoFinal '
- Entra al directorio: 'cd ProyectoFinal'
- Crea y activa un entorio virtual.
- Ejecuta las migraciones: 'python manage.py migrate'
- Inicia el servidor: 'python manage.py runserver'

## Uso

1. Accede a la aplicación desde tu navegador: 'http://127.0.0.1:8000/'
2. Echa un vistazo a la página principal de BeyondGames (inicio), verás las publicaciones más recientes de nuestros usuarios.
3. En la barra de navegación puedes encontrar las opciones:
    * Inicio: Página principal.
    * Sobre nosotros: Datos interesantes sobre los creadores, no te lo pierdas.
    * Publicar: Encontrarás un formulario para crear tu propia publicación cada vez que quieras.
    * Mis publicaciones: Podrás ver las publicaciones que has hecho, así como gestionarlas (ver Detalles, Actualizar o Eliminar).
    * Registrarse: Aquí podrás crear un usuario si lo deseas.
    * Salir: Opción para cerrar tu sesión.

