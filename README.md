# Websockets

A sample websocket server and client.

## Deploying a websocket server

## Installing the virtual environment and dependencies

```shell
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Using supervisor to run the server

Update the file in `deploy_tools/supervisord.conf` with the corresponding paths.

Start supervisor

```shell
source venv/bin/activate
cd deploy_tools
supervisord -c supervisord.conf -n
```

### Deployment with nginx

Copy the file in `deploy_tools/nginx-template.conf` to `/etc/nginx/conf.d/`, modify as necessary.

Check that nginx configuration is correct and restart nginx

```shell
sudo nginx -t
sudo systemctl restart nginx
```

Check that it works correctly by connecting with the client.

```shell
python client.py ws://localhost:8080/  # Assuming that server is listening in localhost:8080
```

### Troubleshooting

If there is a 502 error when connecting to the server, it may be due to nginx not having
the necessary permissions. 

Check nginx logs:

```shell
less /var/log/nginx/error.log
less /var/log/nginx/access.log
```

If there is a permission denied in the logs. Change the ownership of the folder
where the websocket server is installed, and assign permissions to nginx group. 
Nginx group can be named www-data or nginx, check name in `/etc/nginx/nginx.conf` file. Example:


```shell
sudo chown -R daniel:www-data Websocket-Server
sudo chmod g+x Websocket-Server
```

