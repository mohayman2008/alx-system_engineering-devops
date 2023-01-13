# Installs and configure Nginx web server
exec { 'add nginx stable repo':
  path    => $path,
  command => 'sudo add-apt-repository ppa:nginx/stable',
}

# update software packages list
exec { 'apt cache update':
  path    => $path,
  command => 'apt-get update'
}

# Install nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt cache update']
}

# Add firewall rules
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => $path,
  require => Package['nginx']
}

# Chmod
exec { 'chmod www folder':
  path    => $path,
  command => 'chmod -R 755 /var/www'
}

# Create index.html
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Create 404
file { '/var/www/html/404':
  content => "Ceci n'est pas une page\n",
}

# add redirection and error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  notify  => Service['nginx'],
  content =>
'server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
        error_page 404 /404;
        location  /404 {
            internal;
        }
        
        location /redirect_me {
            return 301 https://www.google.com/;
        }
}
'
}

# Restart nginx
exec { 'restart service':
  path    => $path,
  command => 'service nginx restart'
}

# start service nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
