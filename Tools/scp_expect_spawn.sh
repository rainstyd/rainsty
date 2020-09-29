#!/usr/bin/expect

set timeout 30
spawn scp -P 22 -r [lindex $argv 0] root@127.0.0.1:/root/rainsty/[lindex $argv 1]

expect {
        "(yes/no)?"
        {send "yes\n";exp_continue}
        "password:"
        {send "ZSYGMM\n"}
}
interact
