# Kill a commd
exec {'exec_command':
    command => 'pkill killmenow',
    path    => ['/bin', '/usr/bin']
}
