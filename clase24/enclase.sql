SELECT * FROM `usuarios` WHERE edad BETWEEN 18 and 40;

SELECT * FROM `usuarios` WHERE edad >= 18 and edad <= 40;

SELECT * FROM `usuarios` WHERE ocupacion in("estudiante", "ama de casa") order by apellido LIMIT 5,10;


/* join */
SELECT nombre as "N", apellidos, curso
FROM alumnos JOIN cursos

SELECT nombre as "N", apellidos, curso
FROM alumnos JOIN cursos
ON  alumnos.idCurso = cursos.idCurso;

USE curso24166;
SELECT nombre, apellidos, curso FROM alumnos JOIN cursos ON alumnos.idCurso = cursos.idCurso;

/* left Join */
USE curso24166;
SELECT nombre, apellidos, curso FROM alumnos LEFT JOIN cursos ON alumnos.idCurso = cursos.idCurso;

/* right join */
USE curso24166;
SELECT curso 
FROM alumnos RIGHT JOIN cursos 
ON alumnos.idCurso = cursos.idCurso
WHERE apellidos is null
ORDER by apellidos
LIMIT 10
;

/* alumnos cursando */
USE curso24166;
SELECT nombre, apellido, curso FROM alumnos left JOIN cursos ON alumnos.idCurso = cursos.idCurso;

/* alumnos que no estan cursando */
USE curso24166;
SELECT nombre, apellidos FROM alumnos LEFT JOIN cursos ON alumnos.idCurso = cursos.idCurso WHERE curso is null;

/* alumnos totales */
USE curso24166;
SELECT count(apellidos) as 'Cantidad de alumnos que cursan Python'
FROM alumnos JOIN cursos 
ON alumnos.idCurso = cursos.idCurso 
WHERE curso = "Python";

/* count(), max(), min(), avg() */