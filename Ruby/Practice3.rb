#!/bin/ruby

# Let's look at more advanced concepts

class MegaGreeter
  attr_accessor :names

  # Constructor
  def initialize(names = "World")
    @names = names
  end

  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each")
      # Iterate through the list of names
      @names.each do |name|
        puts "Hello, #{name}!"
      end
    else
      puts "Hello, #{names}!"
    end
  end

  def say_bye
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("join")
      # Put the list elements with commas
      puts "Goodbye #{@names.join(", ")}. Come back soon!"
    else
      puts "Goodbye #{@names}. Come back soon!"
    end
  end
end

if __FILE__ == $0
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  mg.names = "Zeke"
  mg.say_hi
  mg.say_bye

  mg.names = ["Albert", "Brenda", "Charles", "Darwin", "Engelbert"]

  mg.say_hi
  mg.say_bye

  mg.names = nil
  mg.say_hi
  mg.say_bye
end
