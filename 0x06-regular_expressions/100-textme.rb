#!/usr/bin/env ruby
print ARGV[0].scan(/from:(\+?\w+)/ ).join + ',' + ARGV[0].scan(/to:(\+?\d+)/).join + ',' + ARGV[0].scan(/flags:(\-?\d:\-?\d:\-?\d:\-?\d:\-?\d)/).join + "\n"
