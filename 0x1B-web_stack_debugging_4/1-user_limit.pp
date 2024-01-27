# puppet manifest to change the user limit

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "s/5/50/; s/4/40/" /etc/security/limits.conf',
  path    => 'usr/local/bin/:/bin/',
}
