# git_leaks

El siguiente código recoge los leaks de un cierto de repositorio de git, buscando entre todos sus commits para dencontrar cuales son los que tiene posibles 
fugas de información o leaks. Ademas hay dos archivos uno, git_leaks.py que lo carga a un .txt y un git_leaks_json.oy que lo carga en un json

Para su correcta ejecución es necesario descargar todo el repositorio y descargar el requirements.txt y posteriormenerte ejecutarlo en una terminal 
de la forma python nombre_del_archivo_a_ejecutar.py donde nombre_del_archivo_a_ejecutar será en este caso git_leaks o git_leaks_json
