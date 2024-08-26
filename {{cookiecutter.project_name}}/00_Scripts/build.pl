{% raw %}#!/usr/bin/perl

use strict;
use warnings;
use Getopt::Long;

# Initialize variable to hold the LaTeX file name with extension
my $tex_file;

# Parse command-line argument
GetOptions("file=s" => \$tex_file) or die "Error in command line arguments\n";

# Check if the LaTeX file name was provided
unless ($tex_file) {
    die "Usage: $0 --file=<LaTeX file (with .tex extension)>\n";
}

# Ensure the file has a .tex extension
unless ($tex_file =~ /\.tex$/) {
    die "Error: The file must have a .tex extension\n";
}

# Remove the extension for commands that don't need it
(my $file_base = $tex_file) =~ s/\.tex$//;

# Step 1: Run pdflatex to generate auxiliary files
print "Running pdflatex...\n";
system("pdflatex  --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder $tex_file") == 0
    or die "Failed to run pdflatex: $!";

# Step 2: Run BibTeX to handle bibliography references
print "Running bibtex...\n";
system("bibtex $file_base") == 0
    or die "Failed to run bibtex: $!";

# Step 3: Run pdflatex two more times to ensure proper cross-referencing
print "Running pdflatex (second pass)...\n";
system("pdflatex  --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder $tex_file") == 0
    or die "Failed to run pdflatex: $!";

print "Running bibtex (second pass)...\n";
system("bibtex $file_base") == 0
    or die "Failed to run bibtex: $!";

print "Running pdflatex (third pass)...\n";
system("pdflatex  --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder $tex_file") == 0
    or die "Failed to run pdflatex: $!";

print "LaTeX compilation complete. Output is $file_base.pdf\n";
{% endraw %}