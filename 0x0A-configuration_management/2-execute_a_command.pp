# This manifest executes a "pkill" command to kill a process named "killmenow"

exec { 'killmenow':
  path    => $path,
  command => "pkill -f killmenow"
}
