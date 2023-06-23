# Websockets

A sample websocket server and client.

## Deploying a websocket server

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
less /var/www/error.log
less /var/www/access.log
```

If there is a permission denied in the logs. Change the user of nginx in `/etc/nginx/nginx.conf`

