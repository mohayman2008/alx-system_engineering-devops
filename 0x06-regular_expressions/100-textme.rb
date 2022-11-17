#!/usr/bin/env ruby
# puts ARGV[0].scan(/(?<=\[from:|to:|flags:).*?\]/).join.gsub(/\]$/, '').gsub(/\]/, ',')
puts ARGV[0].scan(/(?<=(?:from|to|flags):).*?\]/).join.gsub(/\]$/, '').gsub(/\]/, ',')
