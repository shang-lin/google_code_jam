#!/usr/bin/env perl
#
# Set up templates for a round of the Google Code Jam.

if ($#ARGV + 1 < 1) {
  print "usage: $0 <dirname> <number_of_problems>\n";
  exit;
}

my $pathname = shift;
my $np = shift;
$np = 3 unless defined $np;

mkdir($pathname);

for ($i=1; $i <= $np; $i++) {
  my $filename = $pathname . "/" . chr(64 + $i) . ".py";
  if (! -f $filename) {
    print "Copying template to $filename.\n";
    `cp gcj_template.py $filename && chmod +x $filename`;
  }
  else {
    print "$filename already exists.\n";
  }
}

