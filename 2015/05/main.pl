use v5.38;

# Get lines from file
my @lines;
open my $fh, "<", "input.txt"; while (<$fh>) {chomp; push(@lines, $_)} close $fh;

my $nice1 = 0;
for (@lines) { $nice1++ if (m/(?:[aeiou].*){3,}/ && m/(\w)\1+/ && !m/ab|cd|pq|xy/)}
say "Part 1: $nice1";

my $nice2 = 0;
for (@lines) { $nice2++ if (m/(.{2}).*?\1/ && m/(.)(.)\1/)}
say "Part 2: $nice2";
