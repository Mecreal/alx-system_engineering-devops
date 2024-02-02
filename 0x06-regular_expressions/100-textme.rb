#!/usr/bin/env ruby
puts ARGV[0].scan(regex = /\[from:([\w@.]+)\]\s\[to:([\w@.]+)\]\s\[flags:([\w:]+)\]/).join(',')