#!/usr/bin/env ruby
puts ARGV[0].sub(/.*\[from:([^\]]*)\].*\[to:([^\]]*)\].*\[flags:([^\]]*)\].*/, '\1,\2,\3')
