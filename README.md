# tha-gnome-terminator-tools**

Scripts to improve work efficiency using the Gnome Terminator terminal emulator when working with multiple server instances in AWS.

Only one scenario is supported at this moment:

```terminator-ec2-ssh <pattern1> <pattern2>```

will search for EC2 instances by its names and open SSH connections in separate tabs. Wildcards are supported.

### Example:

If our servers are named according to the following pattern: `<prefix>.<environment>.<domain.tld>`, ie:

> app-0.dev.domain.tld
app-1.dev.domain.tld
>
> app-0.rc.domain.tld
app-1.rc.domain.tld
>
> app-0.prod.domain.tld
app-1.prod.domain.tld

then command:

```terminator-ec2-ssh app*dev* app*rc*```

will open Terminator window with all dev and rc servers connected.
