# This file installs flask using puppet 
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
package {'Werkzeug':
  ensure   => 'Werkzeug 2.1.1',
  provider => 'pip3'
}
