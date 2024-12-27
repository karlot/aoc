use v5.38;
use List::Util qw(sum);

# Get lines from file
open my $fh, "<", "input.txt";
my @lines; while (<$fh>) {chomp; push(@lines, $_)} close $fh;

#// ----- TEST DATA -----
# @lines = (
#     '""',
#     '"abc"',
#     '"aaa\"aaa"',
#     '"\x27"',
# );

my $original_lenghts = sum(map(length, @lines));                # Sumarize len of all lines
my $escaped_lengths = sum(map({length(eval($_))} @lines));      # Sumarize len of all lines after eval-ing them (interpreting escapes)
my $extra_escaped = sum(map({length('"'.($_ =~ s/(\W)/\\$1/gr).'"')} @lines));  # Sumarize len of all lines after applying new escaping

say "Part1: " . ($original_lenghts - $escaped_lengths);
say "Part2: " . ($extra_escaped - $original_lenghts);