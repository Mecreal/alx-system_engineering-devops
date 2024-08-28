# 0-strace_is_your_friend.pp

# Ensure the wp-settings.php file uses the correct PHP extension
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  subscribe => Exec['fix-wordpress']
}
