# BBVision-WebScrap
Resultados del Scrap


Hola! Primero que nada, muchas gracias por esta oportunidad, me diverti muchisimo aprendiendo a scrapear.
Paso a explicar lo sucedido con el proyecto.

Intente con varias librerias, tales como BeautifulSoup4 y Selenium, aunque me termine quedando con Scrapy, siento que es mas eficiente para proyectos a gran escala tales como este.
Cosas que no logre hacer: scrapear comentarios y synopsis, esto se debe a que no encontre la manera de hacer que Scrapy, entre indivualmente a cada link y extraiga la informacion desde el mismo. Extraje la informacion desde las paginas donde estan almacenadas todas las peliculas.
Debido a eso, si bien "pude" extraer el genero de las peliculas, no fue extraido de forma correcta, ya que el xpath cambiaba sutilmente dependiendo de la pelicula, lo cual resulto en que muchos peliculas tengan el genero equivocado.

Cosas que me costaron mucho hacer: cambiar de la pagina 1, a la pagina 2 y asi sucesivamente. Debido a que la pagina que me enviaron, el boton de "next" no recibe una clase, es literalmente una url con una imagen de [NEXT] encima, se me hizo extramadamente complicado encontrar la manera de hacer que cambie de pagina, ya que el xpath cambiaba segun la pagina en la que se encuentre scrapeando el scrip actualmente. Hasta que me di cuenta que si iba a la ultima pagina, el xpath del boton de "Previous" siempre recibia el mismo valor que era 'li[2]/a', de esta manera pude, navegar entre las paginas.

Si bien no es el scrap perfecto ni de cerca, me diverti muchisimo haciendolo y me encantaria aprender mas sobre el tema.

Saludos y muchisimas gracias por esta oportunidad!


EL COMANDO PARA EJECUTAR EL SCRIPT ES:

scrapy runspider movies.py -o movies.csv
