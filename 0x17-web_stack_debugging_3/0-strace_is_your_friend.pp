# web stuck debugging using strace, fixing the issue and automate it

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub('.phpp', '.php') %>"),
}
