use v5.38;
use Algorithm::Permute "permute";
use List::Util "max", "min";

# Get lines from file
die "Required one input file as argument!" unless scalar @ARGV == 1;
open my $fh, "<", $ARGV[0] or die $!;
my @lines; while (<$fh>) {chomp; push(@lines, $_)} close $fh;

my %distances = ();
my %towns = ();

for (@lines) {
    my ($src, undef, $dst, undef, $dist) = split;
    $towns{$src} = undef;
    $towns{$dst} = undef;
    $distances{"$src->$dst"} = int($dist);
    $distances{"$dst->$src"} = int($dist);
}

my @town_names = keys %towns;
my $shortest = undef;
my $longest = undef;
permute {
    my $path_len = undef;
    for (my $i = 0; $i < scalar(@town_names)-1; $i++) {
        my ($src, $dst) = ($town_names[$i], $town_names[$i + 1]);
        $path_len += $distances{"$src->$dst"};
    }
    # say join("->", @town_names)." : $path_len";
    $shortest = defined $shortest ? min($shortest, $path_len) : $path_len;
    $longest = defined $longest ? max($longest, $path_len) : $path_len;
} @town_names;

say "Part1: $shortest";
say "Part2: $longest";