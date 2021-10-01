# inf3995-principal

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
