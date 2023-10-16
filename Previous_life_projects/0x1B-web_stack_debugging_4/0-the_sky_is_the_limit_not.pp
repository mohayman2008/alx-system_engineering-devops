# Fixinig the ulimit for nginx server that affect the number of requests that the web server in
# (Project 0x1B Task 0) can handle simulataneously

file {'/etc/default/nginx':
  content => ''
}

exec {'service nginx restart':
  path    => $path,
  require => File['/etc/default/nginx']
}
