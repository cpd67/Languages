#!/bin/ruby

# Classes, variables types
puts "------------------------------------"
puts "Classes, accessors, and mutators oh my!"

# Greeter Classes
# @ = instance variable, $ = global variable, nothing = local variable.
class Greeter

  # Accessor and mutator for the name instance variable
  attr_accessor :name

  # To write separate accessors and mutators:
  # attr_reader :name = accessor
  # attr_writer :name = mutator

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
puts "Accessor: #{greeter.name}"
puts "Mutator: #{greeter.name="Pat"}"

puts "------------------------------------"

puts "What instance methods can I use for my classes?"

# See what kind of methods you can call on a Greeter object
puts Greeter.instance_methods

puts "------------------------------------"
puts "How about instance methods that I defined for my classes?"

# Methods not obtained from superclasses
puts Greeter.instance_methods(false)

puts "------------------------------------"
