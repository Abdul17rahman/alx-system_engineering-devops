# Configures connection without password

file { '~/.ssh/config':
  ensure  => 'file',
  content => "\
Host *
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
