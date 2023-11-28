# Install and configure an Nginx server using Puppet instead of Bash
exec {'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx package
package {'nginx':
  require => Exec['apt-update'],
  ensure  => installed,
}

# Modify nginx configuration
exec {'nginx_config':
  user    => root,
  command => '/usr/bin/echo "Hello World!" | tee /var/www/html/index.html',
}

# Nginx redirection "301 Moved Permanently"
$redirect = '\\\trewrite ^/redirect_me(/*) https://www.google.com permanent;'

exec {'nginx_redirect':
  user      => root,
  command   => "/usr/bin/sed -i '51i ${redirect}' /etc/nginx/sites-available/default",
}

# Restart Nginx server
exec {'nginx_restart':
  user    => root,
  command => '/sbin/service nginx start',
}
