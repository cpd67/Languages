#!/bin/ruby

# Practice Ruby Program
# https://www.ruby-lang.org/en/documentation/quickstart
# https://www.ruby-lang.org/en/about/

puts "------------------------------------"

# Everything in Ruby is an object. Everything.
puts "Everythin in Ruby is an object."
5.times { puts "I told you so!" }

puts "------------------------------------"
puts "Print statement = puts"

# Print statement is 'puts'
puts "Hello, world!";

puts "------------------------------------"
puts "Method definitions and calls"

# Method definitions
def hello
  puts "Hello, world!"
end

# Can call a method with or without the () (if it takes no parameters)
hello
hello()

puts "------------------------------------"
puts "Using \#{placeholder}"
# The #{name} inserts something into a string.
# In this case, the passed parameter 'name'.
def hello(name)
  puts "Hello, #{name}"
end

hello("Earl")

# Default parameters are supported
def hello(name="World")
  puts "Hello, #{name}!"
end

hello
hello()
hello("Pear")

puts "------------------------------------"

# Operator overloading is also supported, as you can clearly see above.
