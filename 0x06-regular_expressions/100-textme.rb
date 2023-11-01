#!/usr/bin/env ruby
puts ARGV[0].dup.sub(/.*\[from:([^\]]*)\].*\[to:([^\]]*)\].*\[flags:([^\]]*)\].*/, '\1,\2,\3')
