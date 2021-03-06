user { "covio":
  ensure => present,
  managehome => true
}

sudo::sudoers { 'worlddomination':
  ensure   => 'present',
  users    => ['covio'],
  runas    => ['root'],
  cmnds    => ['ALL'],
  tags     => ['NOPASSWD'],
}

package { "build-essential":
  ensure => "installed"
}

package { "git":
  ensure => "installed"
}

package { "mercurial":
  ensure => "installed"
}

package { "bzr":
  ensure => "installed"
}

package { "subversion":
  ensure => "installed"
}

package { "libyaml-dev":
  ensure => "installed"
}

package { "sloccount":
  ensure => "installed"
}
