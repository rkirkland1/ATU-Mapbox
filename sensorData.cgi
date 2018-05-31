#!C:\Strawberry\perl\bin\perl.exe
#!/usr/bin/perl
use warnings;
use strict;
use CGI ':standard';
use DBI;
use CGI::Carp qw(fatalsToBrowser);

print header('text/plain;charset=UTF-8');

my $sliderValue= int(param('data'));
my $lower = $sliderValue*12;
my $higher = ($sliderValue+1)*12;

my $Connection = DBI->connect("DBI:SQLite:lake.db") or die $DBI::errstr;
my $query = $Connection->prepare("select * from sensor where counter > $lower and counter<= $higher order by time desc");#"+($sliderValue*4)+"

$query->execute();
	
my @row;
while (@row = $query->fetchrow_array()) {
	print($row[1]."+".$row[3]."+".$row[4]."+".$row[6]."+");
}

$query->finish();
$Connection->disconnect();