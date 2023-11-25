# Configures connection without password

file { '~/.ssh/config':
  content => 'host * \n\tPrefferedAuthentications publickey\n\tIdentitykey ~/.ssh/school\n\tPasswordAuthentication no'
}
