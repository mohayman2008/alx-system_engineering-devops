# This manifest executes a "pkill" command to kill a process named "killmenow"

package { 'Werkzeug':
  ensure   => '2.2.2',
  provider => 'pip3',
  before   => Package['flask']
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
