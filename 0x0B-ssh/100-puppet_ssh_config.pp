# configure a SSH client configuration using puppet

file_line { 'Turn off passwd auth':
          ensure  => 'present',
          path    => '/etc/ssh/ssh_config',
          line    => '   PasswordAuthentication no',
          replace => 'true'
}

file_line { 'Declare identity file':
          ensure  => 'present',
          path    => '/etc/ssh/ssh_config',
          line    => '   IdentityFile ~/.ssh/school',
          replace => 'true',
          match   => ' IdentityFile ~/.ssh/id_rsa'
}
