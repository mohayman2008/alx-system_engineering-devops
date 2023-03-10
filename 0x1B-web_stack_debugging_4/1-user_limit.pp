# Removing "number of opened files" limit for user "holberton" in Project 0x1B Task 1

exec {'remove limits':
    path   => $path,
    command => 'sed -i "/^.*holberton.*nofile.*$/d" "/etc/security/limits.conf"',
  }
