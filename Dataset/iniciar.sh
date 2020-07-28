echo "Iniciando Repositorio"
echo "--------------------------------------"
git init
git status
echo "Añadiendo Los Primeros Archivos"
echo "--------------------------------------"
git add .
git status
echo "Introduce El SSH del repositorio"
echo "--------------------------------------"
read var
git remote add origin $var
echo "Introduce El titulo de La primera Subida"
echo "--------------------------------------"
read var2
git commit -m "${var2}"
git status
echo "Subiendo a ${var}"
echo "--------------------------------------"
git push origin master

