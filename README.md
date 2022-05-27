Primero actualizamos el sistema usando el comando sudo apt update. Luego descargamos el paquete de Docker usando el comando sudo apt install docker-compose
Ya al tener disponible docker, vamos a descargar imagen de Ubuntu usando el comando sudo docker pull ubuntu. Esto nos va a permitir crear contenedores con el sistema operativo Ubuntu y también utilizar esta imagen más adelante en el dockerfile

<img width="479" alt="Screen Shot 2022-05-23 at 12 28 33 PM" src="https://user-images.githubusercontent.com/72221161/170719419-801cd17a-1cd0-4d05-bed8-d4520b63b82f.png">

El primer comando significa que vamos a utilizar una imagen de Ubuntu que acabamos de descargar en la terminal. Adentro de este contenedor, en la línea 2 vamos a actualizar la última versión. Luego vamos a instalar el servicio de Python 3 (-y para darle yes). Ya al tener el servicio de Python, instalamos pip el cual es el packet manager de Python para luego poder instalar los paquetes que necesitamos. Con pip instalamos dash que es para aplicaciones web, pandas para manejar datos, matplotlib para graficas, numpy para operaciones matemáticas y openpyxl para manejar archivos de Excel adentro de Python. Luego en la línea 10 copiamos el archivo Excel que necesitamos y en la línea 11 la aplicación de Python. Luego usamos el comando expose para abrir el puerto 8050 que es el default para Python
En la aplicación de Python, usamos todas las librerías que descargamos en el dockerfile y también el Excel “obesidad.xlsx”
Para subir el servicio, debemos de tener estos dos archivos listos (el dockerfile y el app.py).
Directamente desde la carpeta donde están todos los archivos, debemos construir el docker, para esto usamos el comando sudo docker build -t y le damos el nombre y la versión del contenedor. Yo lo nombre sofia:v01. Aquí se pueden ver como corren todos los pasos que estaban en el dockerfile:

<img width="602" alt="Screen Shot 2022-05-10 at 3 38 01 PM" src="https://user-images.githubusercontent.com/72221161/170720014-2bd74dc9-0143-47db-a565-dc7941ccd3d7.png">

Cuando se construya exitosamente, podemos entonces correr el servicio de docker. Usamos el comando sudo docker run -it -p 80:80 sofia:v01 para correr el servicio de forma interactiva en el puerto 80 y se le indica el contenedor. Luego agregamos python3 app.py para que este comando corra adentro de la terminal y se pueda ejecutar el programa

Al hacer esto, ya nos debe funcionar el contenedor. Para verificar su funcionamiento en un navegador ingresamos en la barra de búsqueda localhost:8050, que es el puerto que habíamos designado para la aplicación. Y ya este nos debe mostrar la página web con el programa de Python funcionando:

<img width="797" alt="Screen Shot 2022-05-10 at 3 43 36 PM" src="https://user-images.githubusercontent.com/72221161/170720061-c48aefc2-beb3-49c5-a04f-04e322f88b7a.png">
