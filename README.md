# docker_freenom_updater
Update 'A' record to freenom dns service on docker.

## How to use

- Build docker image ex. ```sudo build docker -t yourname/freenom```
- Run docker ex.
```
  docker run --name freenom \
      -d --restart=always \
      -v /etc/localtime:/etc/localtime:ro \
      -v /var/log/freenom/:/var/log/freenom/ \
      -v /var/local/freenom/:/var/local/freenom/ \
      yourname/freenom
```
- Change param file with your settings.
