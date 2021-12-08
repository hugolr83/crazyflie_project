# inf3995-principal

## Conventions de codage

1. Écriture C

    - convention: https://www.gnu.org/prep/standards/html_node/Writing-C.html

2. Écriture Python

    - convention: https://www.python.org/dev/peps/pep-0008/

3. Écriture C++

    - convention: https://github.com/isocpp/CppCoreGuidelines

4. Écriture Angular

    - convention: Même convention que LOG2990 - Projet de logiciel d'application Web

## Requis
* Git LFS est nécessaire pour télécharger les vidéos de démonstration [télécharger ici](https://git-lfs.github.com/)
* Après l'installation, ne pas oublier d'exécuter: `git lfs install` 
* En cas de problème de configurations, il est toujours possible de les télécharger directement de l'interface de Gitlab.

## Lancer la solution avec docker-compose
```bash
docker login registry.gitlab.com # login with your Gitlab username and password (only needed once)
xhost +
docker-compose up
```

Liens:
Client: [http://localhost:8080](http://localhost:8080)
Documentation interactive du backend [http://localhost:8000/docs](http://localhost:8000/docs)

## Lancer des test dans 'Client'
```bash
npm run test
```