# Configures connection without password

define resolve() {
    $con = "host *
        \tPrefferedAuthentications publickey
        \tIdentityFile '~/.ssh/school'
        \tPasswordAuthentication no
        "

    file { '~/.ssh/config':
      content => $con,
    }
}
