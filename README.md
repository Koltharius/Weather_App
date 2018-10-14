# Weather App
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/Koltharius/Weather_App.svg?branch=master)](https://travis-ci.org/Koltharius/Weather_App)

Repositorio para el proyecto de la asignatura de IV del curso 18/19

## Descripción del Proyecto
Aplicación web que mostrará información meteorológica de la ciudad deseada.

## Servicios y herramienta que se van a usar
El proyecto será desarrollado utilizando Python y Flask. También voy a usar una base de datos NoSQL para almacenar las distintas ubicaciones de las que se quiere mostrar la información meteorológica. Los datos serán obtenidos realizando llamadas a la api de [OpenWeatherMap](https://openweathermap.org/api). Para testear la aplicación voy a utilizar la librería pytest.

## Integración continua

Como sistema de integración continua he usado [Travis CI](https://travis-ci.org/). Para ello nos registramos en la plataforma, añadimos el archivo [.travis.yml](https://github.com/Koltharius/Weather_App/blob/master/.travis.yml) acorde con nuestra aplicación y seleccionamos desde la plataforma el repositorio que deseamos.

Otra ventaja que nos aporta es la posibilidad de ejecutar los test de forma inmediata, cuando se añade nuevas funcionalidades a la clase que se esta testeando.