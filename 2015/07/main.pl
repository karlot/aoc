use v5.38;
# Unfinished!

# Get lines from file
open my $fh, "<", "input.txt";
my @lines; while (<$fh>) {chomp; push(@lines, $_)} close $fh;

# All our connections
my $d = {};

@lines = (
    "lx -> a",
    "NOT iz -> ja",
    "gz LSHIFT 15 -> hd",
);

for (@lines) {
    if (m/^() -> ()$/) {
        say $1, $2, $3, $4;
    }
}


say "Part1: " . undef;
say "Part2: " . undef;