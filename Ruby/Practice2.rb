#!/bin/ruby

# Classes, variables types
puts "------------------------------------"
puts "Classes"

# Greeter Classes
# @ = instance variable, $ = global variable, nothing = local variable.
class Greeter
  def initialize(name="World")
    @name = name
  end

  def say_hi()
    puts "Hey there, #{@name}"
  end

  def say_bye()
    puts "Bye, #{@name}"
  end
end

# Create a Greeter object
greeter = Greeter.new("Patrick")
greeter.say_hi
greeter.say_bye

puts "------------------------------------"

puts "What instance methods can I use for my classes?"

# See what kind of methods you can call on a Greeter object
puts Greeter.instance_methods

# Methods not obtained from superclasses
puts Greeter.instance_methods(false)

puts "------------------------------------"
