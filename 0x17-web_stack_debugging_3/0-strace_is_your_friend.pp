# Fixing the typo in the wordpress configuration for the project "Web stack debugging #3"

exec { 'fix class-wp-locale.php':
  path    => $path,
  command => 'sed -i "s/phpp/php/g" "/var/www/html/wp-settings.php"'
}
