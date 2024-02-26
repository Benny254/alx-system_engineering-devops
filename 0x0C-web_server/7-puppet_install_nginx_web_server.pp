# Puppet manifest to install nginx
package { 'nginx':
	ensure => installed,
}

file { '/etc/nginx/sites-available/default':
	ensure  => file,
	content => template('nginx/default.erb'),
}

file_line { 'rewrite_redirect':
	ensure => present,
	path   => '/etc/nginx/sites-available/default',
	line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
	require => File['/etc/nginx/sites-available/default'],
}

file { '/var/www/html/index.html':
	ensure  => file,
	content => 'Alx School',
}

service { 'nginx':
	ensure  => running,
	enable  => true,
	require => Package['nginx'],
}
}
