This challenge was very interesting. After setting up my VM, logged in the guest user.
I ran 
    ip addr
and found 10.0.2.15 at port 80
I ran
    ss -tunl
and found port 3306. I ran it and got something which I didn't know what to do about it.
Now I started lookin upon the codes given in the var/www/ folder. I was potentially trying to find any loose end in code, where I could implement SQL injection.
I tried injecting SQL code in the username and password fields, but nothing happened. I even tried to somehow try using it by placing SQL query in one of the note, in one of my account of the note web app. No results.
There is another vulnaribility. On creating a new account, I mistakenly found that it was possible that the password field might remain empty which sign up. But I couldn't exploit it anyhow. I tried injecting a code like changing the role to admin, and also tried changing the user id, but no effect.

Getting no success from all this, I tried finding vulnaribilities in linux. 
    find / -type f -perm -4000 2>/dev/null
Just trying to check what permissions does the guest user have. I checked binary files like ping, but the permission was denied.
I tried removing all passwords from 
    /etc/passwd
but I lack the permissions. Checked out writable files in /etc/ and found none.
Tried to access log files for user authentication, but the permission remained denied.

This challenge was probably the most exciting one, and the one which gave maximnum learnings. But could not solve it. But I am happy to have tried and enjoy such a challenge.