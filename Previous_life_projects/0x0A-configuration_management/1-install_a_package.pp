# This manifest executes a "pkill" command to kill a process named "killmenow"

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
