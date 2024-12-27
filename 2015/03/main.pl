use v5.38;

# Get lines from file
open my $fh, "<", "input.txt";
my @lines = ();
while (<$fh>) { chomp; push(@lines, $_); }
close $fh;

my %seen_p1 = ("0,0" => 1);
my %seen_p2 = ("0,0" => 1);

for (@lines) {
    my @chars = split "", $_;
    my ($x, $y)   = (0, 0); # Part1, Santa's position
    my ($sx, $sy) = (0, 0); # Part2, Santa's position
    my ($rx, $ry) = (0, 0); # Part2, Robo-Santa's position
    
    while (my ($i, $c) = each @chars) {
        # Part 1 - collect all moves as Santa
        $x++ if $c eq ">";
        $x-- if $c eq "<";
        $y++ if $c eq "^";
        $y-- if $c eq "v";
        $seen_p1{"$x,$y"} = 1 unless ($seen_p1{"$x,$y"});

        unless ($i % 2) {
            # Part 2 - Santa moves on even instructions
            $sx++ if $c eq ">";
            $sx-- if $c eq "<";
            $sy++ if $c eq "^";
            $sy-- if $c eq "v";
            $seen_p2{"$sx,$sy"} = 1 unless ($seen_p2{"$sx,$sy"});
        }
        else {
            # Part 2 - Robo-Santa moves on even instructions
            $rx++ if $c eq ">";
            $rx-- if $c eq "<";
            $ry++ if $c eq "^";
            $ry-- if $c eq "v";
            $seen_p2{"$rx,$ry"} = 1 unless ($seen_p2{"$rx,$ry"});
        }
    }
}

say "Part1: " . scalar(keys %seen_p1);
say "Part2: " . scalar(keys %seen_p2);