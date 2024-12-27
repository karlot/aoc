open my $fh, "<", "input.txt";
while(<$fh>) {
    my $floor = 0;
    my $bii = 0;
    my @chars = split "", $_;
    while (my ($i, $value) = each @chars) {
        $floor++ if $value eq "(";
        $floor-- if $value eq ")";
        if ($floor < 0) { $bii = $i + 1 unless($bii); }
    }
    print "Part1: $floor\nPart2: $bii\n";
}