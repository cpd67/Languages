#!/bin/perl

#Practice perl script. 

=begin
This is a big ass comment. 
Like a multi-lined comment in C++.
Or Java.
Or practically *ANY* language out there.
Any questions?
=cut

$age = 4; #Integer scalar
$name = "\"Larry the Lobster\""; #String scalar
$salary = 4.25; #Floating-point scalar

#Have to escape the $ character ("\$").
print "\n$name"." is ".$age." years old and makes "."\$"."$salary"." an hour.\n";

print "How the hell does a lobster make \$4.25 an hour?\n\n";

#Practice with special escape characters
$practice1 = "\UThis should all be uppercased.\n";
$practice2 = "This \Uword\E should be uppercased.\n";
$practice3 = "\uthe \"t\" in \"the\" should be uppercased.\n";
$practice4 = "This is an example of variable interpolation: $practice1";
$practice5 = "This line contains a bell\a.\n";

#Learned that the last statement in a Perl program doesn't need a semicolon.
#Like PHP. 
print "$practice1"."$practice2"."$practice3"."$practice4"."$practice5\n";
print "It sounded like a drop of water.\nThat's probably what that sound is after doing tab completion in the command-line.\n\nLearning stuff. Like a turtle.\n\n";

print "\QI like to call this a cluster ****. Mainly because it bombardes this String with \\s.\n\n";

print "\QThis is probably how they print directory paths so easily.\n";

print "What the hell is a carriage return?\r\n";

print "What is it?\n\n";

print "Knew it. A carriage return moves the cursor to the left again.\n";
print "It also overwrites the text in that spot with whatever needs to go into stdout.\n";




