# AnalisisProyecto

# Integrantes
-Heyer Tinoco
-Juan Gualotuña
-Juan Falconi

# Diapositivas de la primera parte del proyecto: 
https://www.canva.com/design/DAFqRYjzicw/8jLMDnuto-hOJ7VkrrXp1A/edit?utm_content=DAFqRYjzicw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# Bases de datos empleadas: 
## NoSQL
-CouchDb
-MongoDB
## SQL
-MySql
-SQLite Browser
# Temas de Estudio: 
### Eventos Deportivos a Nivel Mundial
### Actividades de Hobbies
### Conciertos y Eventos Publicos
### Eventos o Noticias mundiales

# Fuentes (Adjunatadas en los documentos)
### Accidentes en competiciones de Bicicleta
### Juegos olimpicos estadisticas
### Estadistica Conciertos de Taylor Swift
### Datos de profesionales en el juego League of Legends
### Fertilidad por edad por los años
### Aplicaciones de PlayStore
### Juegos de Steams y caracteristicas
### Estadisticas de suicidio
### Venta de juegos
### Matches de partidos de futbol mundialmente

# Procedimiento de Datos
## Estructura del viaje de Datos: 
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/84c801df-1b25-43f7-a8dd-19427584f663)
## Conversion de datos: 
Primero convertimos los archivos de csv a Json

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/997d2d8e-9731-44fa-879e-6bc8741e2667)

Conectamos mediante Hamachi para insertar datos a un CouchDb:

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/2148a48c-633f-4308-ae81-de4b97ab8add)

Para subir los archivos a Couchdb y Mongo Db  usamos: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/73d80850-0af4-4c01-9c4f-3a6e9473fb1c)

Ahora para conectar archivos de MongoDb y mandarlo a un solo Couch Db usamos: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/0c61d4f3-0b20-4960-b569-e56fc4e32cf1)

Mandamos todos los archivos a un solo CouchDb usando los mismos codigos y la forma de clonar de Couch Db, y tenemos esto en la base: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/5f0f7dfb-c797-4b5c-9504-fd6eb68571d6)

Ahora todo en Couch Db, procedemos a exportar en CSV para poder limpiar datos:

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/1d841ad0-1d42-4d80-a5c1-e6d9a220fb9a)

Ya con los archivos CSV. Procedemos a asegurarnos que no haya columnas ni filas vacias, o limpiando caracteres especiales con los 10 Datasets: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/b51749a0-cb1d-4382-b0e9-d3c6be343b77)

Ahora conectamos a MySql, creando la base de datos y tabla necesaria: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/ab452296-3bcb-41e3-a31a-d2a8fd8f9478)

Ya con la tabla creada, tenemos que insertar los datos usando las librerias correctas: 

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/e2e6a3bc-bee6-440e-b7ac-a87755724121)

Y asi ya tenemos la tabla en la base de datos MySql. Ahora tenemos que repetir el procedimiento con cada tabla, y al final tendremos esta base de datos:

![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/134c8a6f-b3a8-47cb-8ab7-cec25af4a422)

Para asegurarnos la cantidad de archivos, ejecutamos una suma de count de los archivos de todas las tablas y sumamos. 
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/0493057e-7344-4ab6-928a-f7b29039cca1)

Asi podemos verificar que tenemos un total de 1044901 registros en nuestro DataWarehouse de diferentes fuentes.

# Caso de estudio en Grafana 

## JUEGOS OLIMPICOS

![image](https://github.com/OrlandH/AnalisisProyecto/assets/119060037/1e44d600-c17f-416f-bcbb-00a3f71f8360)

En esta estadistica podemos observar que la edad maxima de los competidores es de 34, en el verano de 1900 gano la medalla de oro.

## TAYLOR-CONCIERTO

![image](https://github.com/OrlandH/AnalisisProyecto/assets/119060037/40a0c7d1-a5c6-4b35-8530-1ba5be004582)

En el concierto de Taylor hubo un 76% de boletos vendidos y el numero total de actuacion junto con el Tour fue de 2 en la ciudad de Philadelphia.

## PlayStore-Google

![image](https://github.com/OrlandH/AnalisisProyecto/assets/119060037/d4858e23-e7ed-4c24-8362-8b96fdac3389)

En la PlayStore de google se encontro que 160 cuentas se instalaron una aplicacion de educacion con la calificaión de 2.57 y con un coste de $10.

## JUEGOS OLIMPICOS

![image](https://github.com/OrlandH/AnalisisProyecto/assets/119060037/f6d130b7-19f5-47b7-9625-a1ace30dddab)

En lo juegos olimpicos el menor peso de un participante es de 153 con la edad de 41 años del sexo masculino.

## PlayStore-Google

![image](https://github.com/OrlandH/AnalisisProyecto/assets/119060037/c548285c-6970-4b1f-ae3c-01a3abf04d7a)

EN la playstore de google se realizo una sola isntalación que se realizo el dia 26 de diciembre del 2020.
# Casos estudio en Power Bi Localmente:
## Matches de copas mundiales: 
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/4fd615f9-3d78-436e-9ca3-34a7489255bb)
-En promedio sin importar la fecha, los goles en casa son mucho mayores que el resto.
-Los partidos con mayor numero de goles fue cuando se jugo en España, Alemania y Australia el 27 de Mayo de 1934.
-Los equipos tienen mejor estadistica jugando de casa.
## Conciertos de Taylor internacionalmente:
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/41b39db8-6922-44d5-88d2-927c44114881)
-Viendo las dos graficas, podemos ver que Taylor Swift tiene muchos fans y popularidad en USA
-A pesar de lo popular que es, podemos ver que fracasa en los conciertos o no es rentable en paises como España. 
-El numero de conciertos internacionales es menor a 30 por pais. Siendo el mas alto Australia con 22. Esto podria afectar a la popularidad de Taylor. Y no se expande como deberia.

## Promedio de victorias jugadores profesionales Lol, y region:
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/ba95ce38-1140-4a46-a99c-3be444b0ca67)
Podemos ver que el Promedio de Victorias de los jugadores profesionales sin importar la region es cerca del 50-55% superando las 1000 partidas.
-La mayoria de los jugadores profesionales pertenecen a Europa con un winrate mayor
-Los jugadores profesionales de japon pertenecen solo al 1.65% y sun winrate es cerca del 50% y por debajo de las 1000 partidas
Podemos concluir que a partir de las regiones de latinoamerica baja el nivel de competitividad y profesionalismo para los torneos.
## Porcentaje de jugadores Veteranos profesionales y victorias en Lol
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/cc1ce6d9-fe25-45c8-a199-ac08a4191453)
-Los veteranos de la region de euw1 son los que tienen mas porcentaje de victorias entre los veteranos
-Estadisticamente, los jugadores nuevos son mucho mejor que los jugadores veteranos en porcentaje de win y Primeras Sangre
-Euw y Korea son las regiones con mejores jugadores pro player.
## Aplicaciones pagadas y gratis populares en PlayStore
![image](https://github.com/OrlandH/AnalisisProyecto/assets/117741739/31a2457d-ee07-495f-aa6f-436b711be2ed)
-Podemos ver que las aplicaciones dominantes en gratuidad por rating es Educational, Music&Audio y Tools
-En promedio las aplicaciones de citas tienen mas rating en forma pagada que gratuito
-Las aplicaciones mas acaras en promedio son las Medicinales
-Las aplicaciones de citas son 4tas en precio alto, y los que triunfan mas en la hora de ser apps pagadas. Asi que es una buena opcion al momento de generar algo de dinero
# Casos estudio en Power Bi en la nube
## Promedio de suicidos entre dos generaciones
![Captura de pantalla 1](https://github.com/OrlandH/AnalisisProyecto/assets/102696740/35359b77-26df-40bf-ac1c-69660d31c33f)
## Juegos con mayor promedio de ventas en la plataforma PS4
![Captura de pantalla 2](https://github.com/OrlandH/AnalisisProyecto/assets/102696740/2d1e675c-0383-4073-90a9-d6e9d7ffe14e)
## Promedio de compras en juegos en la plataforma de PC
![Captura de pantalla 3](https://github.com/OrlandH/AnalisisProyecto/assets/102696740/51117c2a-facd-4cf3-9359-39bb3352c2f1)
## Promedio de goles como local en el entretiempo y promedio de goles como visitante en el entretiempo
![Captura de pantalla 4](https://github.com/OrlandH/AnalisisProyecto/assets/102696740/d9a2a059-2c0d-481f-a8aa-197184009cff)
##  Promedio de suicidos entre EEUU y Uruguay
![Captura de pantalla 5](https://github.com/OrlandH/AnalisisProyecto/assets/102696740/8887085d-cf96-442e-a545-132b8f72a85c)

# Conclusiones: 
En conclusión, la combinación de Python, SQL y Power BI se erige como una alianza poderosa en el ámbito del análisis de datos. Python, con su versatilidad y amplia gama de bibliotecas, proporciona la capacidad de manipular y entender los datos de manera eficiente. SQL, por su parte, es esencial para acceder y gestionar datos en bases de datos relacionales, permitiendo consultas y uniones de datos cruciales para el análisis.
En resumen, esta trinidad de tecnologías proporciona un enfoque integral para el análisis de datos, desde la extracción y procesamiento inicial hasta la presentación de hallazgos de manera efectiva. La sinergia entre estas herramientas es esencial en un mundo cada vez más orientado hacia la toma de decisiones basada en datos, capacitando a profesionales y empresas para aprovechar al máximo la riqueza de información contenida en sus conjuntos de datos y resolver problemas complejos de manera informada y eficaz.
