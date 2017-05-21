# Web-Access-Log-Files-Filtering
Use Python regular expressions to filter Web access logs.

The file access_log.txt is from a security researcher who set up a ‘honeypot’ server to attract hackers, in order to record the HTTP requests used in hacking attempts, to learn about their methods and origins.

The goal is to create two files: 

(a) A summary file that contains the counts of all valid daily visits to each top-level domain. The rows should be ordered in chronological order, and the columns should be sorted in alphabetical order of top-level domains.  The file should be tab-delimited.

(b) A ‘suspicious entries’ file with the actual invalid access rows filtered from the original log, according to the criteria below.

For example, this line in the log counts as a valid visit to the ‘hu’ top-level domain.

195.82.31.125 - - [09/Mar/2004:22:03:09 -0500] "GET http://www.goldengate.hu/cgi-bin/top/topsites.cgi?an12 HTTP/1.0" 200 558 "http://Afrique" "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"

The 'hu' part in the hostname www.goldengate.hu is the top-level domain (representing the country of Hungary). The status code of '200' tells us that the visit was successful. So the line should be counted as a valid visit for the 'hu'domain on 09/Mar/2004.  Note that the top-level domain for a hostname like www.cocegas.com.br is .br, not .com.

Use the following rules to determine if a line should be as a valid line.  A line in the log file represents a valid visit only if these conditions are true:

- The HTTP verb is GET or POST (uppercase).
- ANDthe status code is 200
- ANDthe URL being accessed starts with http:// or https:// (lower-case) followed by at least one alphabetic character (i.e. not a digit or a symbol).  For example, the URL should NOT start with 'http:///', which is an error.
- ANDthe top-level domain consists of only letters. This is to say, if the host name is actually
- a numerical IP address like '202.96.254.200', we don’t count it. If the whole domain name is just '.com' as in http://.com/blah or does not even contain a dot as in http://c/blah, we do not count it. 

As an example, note that we do not count lines like the following as valid:
68.48.142.117 - - [09/Mar/2004:22:41:42 -0500] "GET /scripts/..%c1%9c../winnt/system32/cmd.exe?/c+dir HTTP/1.0" 200 566 "-" "-"

This is because /scripts/ obviously doesn't look like a web address since it doesn’t start with http:// or https:// ). This is a prime example of an attempt to get a file stored locally on that proxy server to exploit vulnerabilities. 

