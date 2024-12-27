perl -e 'while(<>){$n1++ if m/(?:[aeiou].*){3,}/ && m/(\w)\1+/ && !m/ab|cd|pq|xy/; $n2++ if m/(.{2}).*?\1/ && m/(.)(.)\1/} print "p1:$n1, p2:$n2\n"' < input.txt
