use v5.38;

# Get lines from file
open my $fh, "<", "input.txt";
my @lines; while (<$fh>) {chomp; push(@lines, $_)} close $fh;

sub get_light_array($size) {
    my @lights;
    for my $y (0 .. $size - 1) {
        for my $x (0 .. $size - 1) {
            $lights[$y][$x] = 0;
        }
    }
    return \@lights;
}

sub process_ops($ops, $lights1, $lights2) {
    for my $line ($ops->@*) {
        if ($line =~ m/^([\w ]+) (\d+),(\d+) through (\d+),(\d+)$/) {
            my ($op, $x1, $y1, $x2, $y2) = ($1, int($2), int($3), int($4), int($5));
            for my $y ($y1 .. $y2) {
                my $row1 = $lights1->[$y];
                my $row2 = $lights2->[$y];
                for my $x ($x1 .. $x2) {
                    if ($op eq "turn on") {
                        $row1->[$x] = 1;
                        $row2->[$x]++;
                    }
                    elsif ($op eq "turn off") {
                        $row1->[$x] = 0;
                        $row2->[$x]-- if $row2->[$x];
                    }
                    else {
                        $row1->[$x] = $row1->[$x] ? 0 : 1;
                        $row2->[$x] += 2;
                    }
                }
            }
        }
    }
}

sub count($lights) {
    my $count = 0;
    for my $row ($lights->@*) {
        for my $val ($row->@*) {
            $count += $val;
        }
    }
    return $count;
}


my $lights_p1 = get_light_array(1000);
my $lights_p2 = get_light_array(1000);
process_ops(\@lines, $lights_p1, $lights_p2);

say "Part1: " . count($lights_p1);
say "Part2: " . count($lights_p2);