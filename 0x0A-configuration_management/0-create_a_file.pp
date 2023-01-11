# This manifest creates a file 'school' in the directory '/tmp'.

file { 'create a file':
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
