# Configures connection without password

file { 'config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => "\
Host *
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
