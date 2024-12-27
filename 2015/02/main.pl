use v5.38;
use List::Util "min";

open my $fh, "<", "input.txt";
my $total_paper_area = 0;
my $total_ribbon_len = 0;

while(<$fh>) {
    chomp;
    my ($l, $w, $h) = map(int, split("x", $_));
    $total_paper_area += 2*$l*$w + 2*$w*$h + 2*$h*$l + min($l*$w, $w*$h, $h*$l);

    my @slwh = sort { $a <=> $b } ($l, $w, $h);
    $total_ribbon_len += 2*$slwh[0] + 2*$slwh[1] + $l*$w*$h;
}
close $fh;

say "Part1: $total_paper_area";
say "Part2: $total_ribbon_len";