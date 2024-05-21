CREATE DATABASE IF NOT EXISTS maradona

CREATE DATABASE curso24166 
DROP DATABASE curso-24166

CREATE TABLE `curso-24166`.`alumnos` ( `dni` INT(11) NOT NULL ,  `nombre` VARCHAR(30) NOT NULL ,  `apellido` VARCHAR(30) NOT NULL ,  `fecha_nac` DATE NOT NULL ) ENGINE = MyISAM;

ALTER TABLE `alumnos` ADD `id` INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);

/* eliminar */
DROP TABLE ` alumnos `
/* vaciar */
TRUNCATE TABLE `alumnos`


/* DML */

INSERT INTO `curso24166`.`alumnos` (`id`, `dni`, `nombre`, `apellido`, `fecha_nac`) VALUES (1, 32345345, 'Juan', 'Lopez', 1990-05-20);

INSERT INTO `alumnos` (`id`, `dni`, `nombre`, `apellido`, `fecha_nac`) VALUES ('0', '22456775', 'Pedro', 'Marmol', '1991-05-21'), ('10', '2323424', 'Marcela', 'Morelo', '1981-01-23'); 

UPDATE `alumnos` SET `dni` = '29323000' WHERE `alumnos`.`id` = 10;
UPDATE `alumnos` SET `apellido` = '' WHERE `alumnos`.`id` = 3;

DELETE FROM `alumnos` WHERE `alumnos`.`id` = 3

SELECT * FROM `alumnos`
SELECT dni, nombre, apellido FROM `alumnos` WHERE id > 9
SELECT dni, nombre, apellido FROM `alumnos` WHERE id = 1
SELECT dni, nombre, apellido FROM `alumnos` WHERE nombre = "Juan"

SELECT nombre, apellido, email FROM `usuarios` WHERE edad > 18 and edad < 30