# Install and configure an Nginx server using Puppet instead of Bash
exec {'apt-update':
  command => '/usr/bin/apt-get update'
}

# Install nginx package
package {'nginx':
  require => Exec['apt-update'],
  ensure  => installed,
}

# Add a custom header
exec {'http_header':
  user      => root,
  command   => "sudo sed -i '/server_name _/a \\    add_header X-Served-By \$HOSTNAME;' /etc/nginx/sites-available/default",
}

# Restart Nginx server
service {'nginx':
  ensure  => running,
  require => Exec['http_header'],
}
