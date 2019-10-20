# Cyber Crime Cup

## Links
* [Team Dashboard](https://www.cybercrime.co.uk/dashboard-team)
* [Challenge Dashboard](https://www.cybercrime.co.uk/dashboard-challenges)

## Useful commands
* wfuzz form for tty: `wfuzz --oF wfuzz-log -u http://3.cybertrial.co.uk/login -b "PHPSESSID=rk1meepo069lvoo34udt5agqgn" -d "formgo=1&username=FUZZ&password=test" -t 1 -s 0.7 -w [WORDLIST] --hs [IGNORE_STRING] -c`
* run in background: `nohup [COMMAND_STRING] &`
