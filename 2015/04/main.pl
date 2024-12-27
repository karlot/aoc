use v5.38;
use Digest::MD5 "md5_hex";

open my $fh, "<", "input.txt" or die "Cannot open input file";
my $key = <$fh>;
chomp($key);

sub find_number($zeroes) {
    my $search_target = "0" x $zeroes;
    my $number = 0;
    while(1) {
        return $number if (md5_hex($key, $number) =~ /^$search_target/);
        $number++;
    }
}

say "Part1: " . find_number(5);
say "Part2: " . find_number(6);