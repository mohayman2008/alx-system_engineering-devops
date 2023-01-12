# This manifest configures SSH client to connect to a server without typing a password
#  and use '~/.ssh/school' as private key
include stdlib

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
